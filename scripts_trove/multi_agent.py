import os
import json
import logging
import requests
from dotenv import load_dotenv
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import matplotlib.pyplot as plt

# Load API keys from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load OpenAI API Key and FMP API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")

# Validate API Keys
if not OPENAI_API_KEY:
    logging.error("ERROR: OpenAI API Key not found! Ensure it is set in env/.env")
    exit(1)

if not FMP_API_KEY:
    logging.error("ERROR: Financial Modeling Prep API Key not found! Ensure it is set in env/.env")
    exit(1)

logging.info("OpenAI API Key loaded successfully.")
logging.info("Financial Modeling Prep API Key loaded successfully.")

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

# Fetch financial data from FMP API
company_name = "Tesla"
api_url = f"https://financialmodelingprep.com/api/v3/income-statement/TSLA?apikey={FMP_API_KEY}"

logging.info(f"Fetching financial data for {company_name}...")

try:
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    financial_data = response.json()
    logging.info("Successfully retrieved financial data.")
except requests.exceptions.RequestException as e:
    logging.error(f"ERROR: Failed to fetch financial data - {str(e)}")
    exit(1)

# Extract key financial metrics
if isinstance(financial_data, list) and len(financial_data) > 0:
    latest_financials = financial_data[0]
else:
    logging.error("ERROR: No valid financial data found!")
    exit(1)

revenue = latest_financials.get("revenue", 0)
net_profit = latest_financials.get("netIncome", 0)
debt_equity_ratio = latest_financials.get("totalDebt", 0) / max(latest_financials.get("totalEquity", 1), 1)
cash_flow = latest_financials.get("operatingCashFlow", 0)


# --------------- MOA Implementation --------------- #

class TroveAgent:
    """Basic agent structure for the MOA framework."""
    
    def __init__(self, agent_name, task_description):
        self.agent_name = agent_name
        self.task_description = task_description

    def run(self, data):
        """Simulates processing the given task and returns an analysis."""
        logging.info(f"{self.agent_name} executing task...")
        return f"{self.task_description}\n\nFindings:\n- Processed data: {data}"


class TroveMOA:
    """Implements the Mixture-of-Agents (MOA) system."""
    
    def __init__(self, name, agents):
        self.name = name
        self.agents = agents
        self.intermediate_results = []

    def run(self, data):
        """Runs the MOA framework step-by-step."""
        logging.info(f"Running MOA framework: {self.name}")

        # Process each agent's task
        for agent in self.agents:
            result = agent.run(data)
            self.intermediate_results.append(result)
            logging.info(f"Completed task: {agent.agent_name}")

        # Aggregate all results
        final_report = "\n\n".join(self.intermediate_results)
        return final_report


# Define Agents
financial_agent = TroveAgent(
    agent_name="FinancialStatementAnalyzer",
    task_description=f"Analyze Tesla's financial performance:\n- Revenue: ${revenue:,}\n- Net Profit: ${net_profit:,}"
)

risk_agent = TroveAgent(
    agent_name="RiskAssessmentSpecialist",
    task_description="Assess Tesla's financial and market risks:\n- Debt-to-Equity Ratio\n- Market Volatility\n- Regulatory Challenges"
)

strategy_agent = TroveAgent(
    agent_name="BusinessStrategyEvaluator",
    task_description="Evaluate Tesla's business strategy:\n- Competitive Advantage\n- Growth Potential\n- Expansion Plans"
)

aggregator_agent = TroveAgent(
    agent_name="ReportAggregator",
    task_description="Aggregate all findings into a structured report."
)

# Initialize and Run MOA
moa = TroveMOA(
    name="Tesla-MOA-Analysis",
    agents=[financial_agent, risk_agent, strategy_agent, aggregator_agent]
)

final_analysis_report = moa.run(data=f"Revenue: ${revenue:,}, Net Profit: ${net_profit:,}, Debt-to-Equity: {debt_equity_ratio:.2f}, Cash Flow: ${cash_flow:,}")

logging.info("\nFinal MOA Analysis Report:\n" + final_analysis_report)


# --------------- Generate PDF Report --------------- #

def generate_financial_chart():
    """Generates a bar chart visualizing Tesla's key financial metrics."""
    categories = ["Revenue", "Net Profit", "Debt/Equity", "Cash Flow"]
    values = [revenue, net_profit, debt_equity_ratio, cash_flow]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=["blue", "green", "red", "orange"])
    plt.xlabel("Metrics")
    plt.ylabel("Value (in USD Millions)")
    plt.title(f"Financial Metrics for {company_name}")
    plt.grid(axis="y", linestyle="--")
    plt.savefig("reports/tesla_financial_chart.png")
    logging.info("Financial trend chart saved as 'reports/tesla_financial_chart.png'")


def generate_pdf_report(report_text, filename="reports/tesla_financial_report.pdf"):
    """Generates a detailed PDF report."""
    generate_financial_chart()
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Helvetica", "", 14)

    pdf.cell(200, 10, f"{company_name} Financial Analysis Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(10)

    pdf.multi_cell(0, 10, report_text)
    pdf.ln(10)

    pdf.cell(200, 10, "Key Financial Metrics", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(5)

    pdf.multi_cell(0, 10, f"Revenue: ${revenue:,}\nNet Profit: ${net_profit:,}\nDebt-to-Equity Ratio: {debt_equity_ratio:.2f}\nCash Flow: ${cash_flow:,}")
    pdf.ln(10)

    pdf.cell(200, 10, "Financial Trends Chart", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
    pdf.ln(5)

    pdf.image("reports/tesla_financial_chart.png", x=10, y=None, w=180)

    pdf.output(filename, dest='F')
    logging.info(f"Financial report saved as {filename}")


# Execute Report Generation
generate_pdf_report(final_analysis_report)
