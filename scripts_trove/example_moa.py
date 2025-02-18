import os
import sys
import json
import requests
import logging
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from fpdf import FPDF

# Ensure script runs from the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents_trove.trove_agent import TroveAgent
from agents_trove.trove_agent_moa import TroveMOA

# Load API keys from environment variables
load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")

# Configure Logging
log_filename = "logs/tesla_moa_analysis.log"
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=log_filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Ensure reports directory exists
os.makedirs("reports", exist_ok=True)

# Check API Key Availability
if not OPENAI_API_KEY:
    logging.error("ERROR: OpenAI API key not found! Ensure it's set in .env file.")
    raise ValueError("ERROR: OpenAI API key not found!")
else:
    logging.info("✅ OpenAI API Key loaded successfully.")

if not FMP_API_KEY:
    logging.error("ERROR: Financial Modeling Prep (FMP) API key not found! Ensure it's set in .env file.")
    raise ValueError("ERROR: FMP API key not found!")
else:
    logging.info("✅ Financial Modeling Prep API Key loaded successfully.")

# Fetch Tesla financial data
company_name = "Tesla"
api_url = f"https://financialmodelingprep.com/api/v3/income-statement/TSLA?apikey={FMP_API_KEY}"

try:
    logging.info(f"🔍 Fetching financial data for {company_name}...")
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    financial_data = response.json()
    logging.info("✅ Successfully retrieved financial data.")
except requests.exceptions.RequestException as e:
    logging.error(f"❌ ERROR: Failed to fetch financial data - {str(e)}")
    raise ValueError(f"ERROR: Failed to fetch financial data - {str(e)}")

if isinstance(financial_data, list) and len(financial_data) > 0:
    latest_financials = financial_data[0]
else:
    raise ValueError("ERROR: No valid financial data found!")

# Extract key financial metrics
revenue = latest_financials.get("revenue", 0)
net_profit = latest_financials.get("netIncome", 0)
debt_equity_ratio = latest_financials.get("totalDebt", 0) / max(latest_financials.get("totalEquity", 1), 1)
cash_flow = latest_financials.get("operatingCashFlow", 0)

# Define Agents with proper output
financial_agent = TroveAgent(
    agent_name="FinancialStatementAnalyzer",
    system_prompt=f"""
    **Financial Performance Analysis for Tesla**
    - Revenue: ${revenue:,}
    - Net Profit: ${net_profit:,}
    - Debt-to-Equity Ratio: {debt_equity_ratio:.2f}
    - Cash Flow: ${cash_flow:,}

    **Analysis Summary:**
    - Tesla’s revenue trend over the last 5 years and its implications.
    - Profitability analysis: What is driving Tesla’s profits?
    - Debt sustainability and financial stability.
    - Investment potential based on Tesla’s financial metrics.
    """,
    llm="gpt-4o",
)

risk_agent = TroveAgent(
    agent_name="RiskAssessmentSpecialist",
    system_prompt="""
    **Risk Assessment for Tesla**
    - Market Risks: EV industry trends, global demand, and competitive landscape.
    - Financial Risks: Debt exposure, profitability volatility, and economic downturns.
    - Regulatory & Compliance Risks: Government policies and environmental regulations.
    - Supply Chain Risks: Lithium-ion battery supply constraints and global shortages.

    **Mitigation Strategies:**
    - How Tesla can reduce market volatility impacts.
    - Strategies for managing financial risks.
    - Compliance with evolving EV regulations.
    """,
    llm="gpt-4o",
)

strategy_agent = TroveAgent(
    agent_name="BusinessStrategyEvaluator",
    system_prompt="""
    **Tesla's Business Strategy & Growth Prospects**
    - Expansion into new markets (India, Southeast Asia, etc.).
    - Competitive positioning vs. rivals (BYD, Lucid Motors, legacy automakers).
    - Future growth areas: Energy storage, AI-driven autonomous driving, and software sales.
    - R&D and Innovation: AI, self-driving technology, battery advancements.

    **Strategic Recommendations:**
    - How Tesla can maintain long-term industry leadership.
    - Innovation roadmap: Where should Tesla invest next?
    - Scaling production to meet rising EV demand.
    """,
    llm="gpt-4o",
)

aggregator_agent = TroveAgent(
    agent_name="ReportAggregator",
    system_prompt=f"""
    Generate a **structured 10-page business analysis report** for Tesla:
    - **Company Overview**: Tesla’s history, achievements, and market positioning.
    - **Financial Performance**: Revenue, net profit, debt-equity trends over 5 years.
    - **Risk Analysis**: Market, regulatory, and financial risks with mitigation strategies.
    - **Business Strategy Evaluation**: Tesla’s competitive edge and future roadmap.
    - **Industry Trends**: Global EV sector growth and Tesla’s market share.
    - **Future Outlook & Recommendations**: Strategic investment opportunities.
    - **Data Insights & Visualization**: Graphs, charts, and key financial trends.
    """,
    llm="gpt-4o",
)

# Initialize the MOA System
moa = TroveMOA(
    name="Trove-MOA-TeslaAnalysis",
    agents=[financial_agent, risk_agent, strategy_agent],
    layers=2,
    final_agent=aggregator_agent,
)

# Execute the Analysis and Capture Detailed Outputs
logging.info(f"🚀 Running Tesla Business Analysis...")

financial_output = financial_agent.run("Generate detailed financial insights for Tesla.")
risk_output = risk_agent.run("Analyze Tesla's risk factors and mitigation strategies.")
strategy_output = strategy_agent.run("Evaluate Tesla's business strategy and future opportunities.")
final_report = moa.run(f"Generate a comprehensive business analysis report for {company_name}.")

# Data Visualization
categories = ["Revenue", "Net Profit", "Debt/Equity", "Cash Flow"]
values = [revenue, net_profit, debt_equity_ratio, cash_flow]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=["blue", "green", "red", "orange"])
plt.title(f"Financial Metrics for {company_name}")
plt.xlabel("Metrics")
plt.ylabel("Value (in USD Millions)")
plt.savefig("reports/tesla_financial_chart.png")
logging.info("📊 Financial data visualization saved.")

# Generate and Save Report as PDF
pdf_filename = f"reports/{company_name.replace(' ', '_').lower()}_moa_report.pdf"
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, f"{company_name} Business Analysis Report", ln=True, align="C")

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Financial Analysis", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, financial_output.encode("latin-1", "replace").decode("latin-1"))

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Risk Assessment", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, risk_output.encode("latin-1", "replace").decode("latin-1"))

pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Business Strategy Evaluation", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, strategy_output.encode("latin-1", "replace").decode("latin-1"))

pdf.image("reports/tesla_financial_chart.png", x=10, y=pdf.get_y() + 10, w=170)
pdf.output(pdf_filename)

logging.info(f"✅ Final report saved: {pdf_filename}")
print(f"📄 Final Report saved as PDF: {pdf_filename}")
