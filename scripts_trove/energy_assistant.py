import openai
import json
import os
import sys
import matplotlib.pyplot as plt
from fpdf import FPDF
from dotenv import load_dotenv

# Add module paths
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(base_dir, 'agents_trove'))
sys.path.append(os.path.join(base_dir, 'tools_trove'))
data_path = os.path.join(base_dir, 'data_trove', 'energy_data.json')

from trove_agent import TroveAgent  # Import the TroveAgent class from agents_trove folder
from efficiency_tool import calculate_efficiency  # Import efficiency tool from tools_trove folder

# Load environment variables from an .env file
load_dotenv(os.path.join(base_dir, "env", ".env"))

# Load OpenAI API Key Securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("❌ ERROR: OpenAI API key not found!")
    print("➡️  Please set it in the env/.env file as OPENAI_API_KEY='your-api-key'")
    exit(1)

# Initialize OpenAI client correctly with API key
client = openai.OpenAI(api_key=OPENAI_API_KEY)

class EnergyAssistant(TroveAgent):
    """
    A specialized agent that analyzes energy consumption data and provides efficiency recommendations using an LLM.
    """

    def __init__(self):
        super().__init__(agent_name="EnergyAssistant",
                         system_prompt="You are an expert in energy consumption analysis.",
                         llm="OpenAIChat",
                         autosave=True,
                         verbose=True)

        # Load historical energy data from a JSON file
        self.load_energy_data(data_path)

        # Add a tool for calculating energy efficiency
        self.add_tool("calculate_efficiency", calculate_efficiency)

    def load_energy_data(self, file_path):
        """Loads past energy data into the agent's long-term memory."""
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.long_term_memory["energy_data"] = data
                self.input_data_json = json.dumps(data, indent=4, ensure_ascii=False)  # Store JSON formatted data
                self.input_data_table = data[:10]  # Store first 10 records for tabular format
                print(f"Loaded {len(data)} energy records into memory.")
        else:
            print(f"❌ ERROR: Energy data file not found at {file_path}! Please ensure 'energy_data.json' exists.")
            exit(1)

    def analyze_energy_trends(self):
        """Retrieves past energy data and requests insights from the LLM."""
        if "energy_data" not in self.long_term_memory:
            print("⚠️ No historical energy data found.")
            return "No historical energy data found."

        # Retrieve last 25 records
        recent_data = self.long_term_memory["energy_data"][-25:]

        # Format data as a prompt for LLM
        prompt = f"""
        Here is the recent energy consumption data:
        {recent_data}
        Based on these patterns, suggest ways to improve energy efficiency.
        """

        # Use OpenAI's updated API call format
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    def execute_tool(self, tool_name, params):
        """Executes the specified tool and returns the result."""
        if tool_name in self.tools:
            return self.tools[tool_name](**params)
        return f"⚠️ Tool '{tool_name}' not found."

    def generate_visuals(self):
        """Generates detailed graphs and charts for the energy data."""
        if "energy_data" not in self.long_term_memory:
            print("⚠️ No energy data available for visualization.")
            return None

        data = self.long_term_memory["energy_data"]
        dates = [entry["date"] for entry in data]
        consumption = [entry["consumption"] for entry in data]
        production = [entry["production"] for entry in data]

        plt.figure(figsize=(12, 6))
        plt.plot(dates, consumption, label='Energy Consumption (kWh)', marker='o', linestyle='-')
        plt.plot(dates, production, label='Energy Production (kWh)', marker='s', linestyle='--')
        plt.xlabel("Date")
        plt.ylabel("Energy (kWh)")
        plt.title("Energy Consumption vs. Production Trend")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("energy_trend.png")
        print("📊 Graph saved as 'energy_trend.png'")

    def generate_pdf_report(self, report_text, efficiency_result, filename="energy_report.pdf"):
        """Generates a highly detailed and elegant PDF report with a tabular representation of input data."""
        self.generate_visuals()

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", "B", 18)
        pdf.cell(200, 10, "Energy Consumption Report", ln=True, align="C")
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Energy Analysis & Insights", ln=True, align="C")
        pdf.ln(5)
        
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, report_text)
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Efficiency Analysis", ln=True, align="C")
        pdf.ln(5)
        
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, efficiency_result)
        pdf.ln(10)
        
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, "Visual Analysis", ln=True, align="C")
        pdf.ln(5)
        
        pdf.image("energy_trend.png", x=10, y=None, w=180)
        
        pdf.output(filename, dest='F')
        print(f"📄 Report saved as {filename}")

if __name__ == "__main__":
    # Instantiate the Energy Assistant
    energy_agent = EnergyAssistant()

    # Run energy analysis
    report = energy_agent.analyze_energy_trends()
    print("\n🔹 Energy Consumption Report 🔹\n", report)

    # Run the efficiency calculation tool
    efficiency_result = energy_agent.execute_tool("calculate_efficiency", {"consumption": 500, "production": 600})
    print("\n⚡ Energy Efficiency Calculation ⚡\n", efficiency_result)

    # Generate and save the PDF report
    energy_agent.generate_pdf_report(report, efficiency_result)
