import os
import logging
from agents_trove.trove_agent import TroveAgent

class TroveMOA:
    """
    Mixture-of-Agents (MOA) class implementing a multi-layered agent processing system.
    Ensures structured logging, indexed execution, and meaningful output.
    """

    def __init__(self, name, agents, layers, final_agent):
        """
        Initializes the MOA system.
        
        :param name: Name of the MOA instance
        :param agents: List of TroveAgent objects
        :param layers: Number of processing layers
        :param final_agent: Final agent responsible for summarizing results
        """
        self.name = name
        self.agents = agents
        self.layers = layers
        self.final_agent = final_agent
        self.intermediate_results = []
        
        # Configure logging
        log_filename = f"logs/{self.name}_execution.log"
        os.makedirs("logs", exist_ok=True)
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logging.info(f"✅ Initialized MOA system: {self.name}")

    def run(self, task):
        """
        Executes the MOA system by processing the task through multiple layers.
        
        :param task: The input task for processing
        :return: Final output after all agents have processed the task
        """
        logging.info(f"🚀 Starting MOA execution for task: {task}")
        current_task = task

        for layer in range(self.layers):
            logging.info(f"📌 Processing Layer {layer + 1}/{self.layers}")
            layer_results = []

            for agent in self.agents:
                logging.info(f"🔍 Agent {agent.agent_name} executing task...")
                result = agent.run(current_task)

                if not result:
                    logging.error(f"❌ Agent {agent.agent_name} returned an empty response!")
                    result = f"⚠️ No data available from {agent.agent_name}."

                logging.info(f"✅ Agent {agent.agent_name} completed task. Preview: {result[:200]}...")
                layer_results.append(result)

            self.intermediate_results.append(layer_results)
            current_task = "\n\n".join(layer_results)  # Aggregate results

        # Final agent processes the aggregated results
        logging.info("🔹 Final agent aggregating and summarizing results...")
        final_result = self.final_agent.run(current_task)

        if not final_result:
            logging.error("❌ Final agent returned an empty report!")
            final_result = "⚠️ Report generation failed. Please check logs for more details."

        logging.info("✅ MOA execution completed successfully.")
        return final_result


# 🏢 **Define Agents with Detailed Prompts**
financial_agent = TroveAgent(
    agent_name="FinancialStatementAnalyzer",
    system_prompt="""
    Provide an **in-depth financial analysis** for Indian and global companies:
    - Key metrics: **Revenue, Net Profit, EBITDA, Debt-to-Equity ratio**.
    - Analyze **trends over the past 5 years**.
    - Assess **financial risks, growth opportunities, and profitability**.
    - Evaluate **investment feasibility and financial health**.
    """,
    llm="gpt-4o",
)

risk_agent = TroveAgent(
    agent_name="RiskAssessmentSpecialist",
    system_prompt="""
    Conduct a **comprehensive risk analysis**:
    - **Market Risks**: Competitive threats, economic instability, inflation impact.
    - **Regulatory & Compliance**: Government policies, tax laws, industry regulations.
    - **Operational Risks**: Supply chain disruptions, workforce challenges, technological obsolescence.
    - Suggest **risk mitigation strategies** for long-term sustainability.
    """,
    llm="gpt-4o",
)

strategy_agent = TroveAgent(
    agent_name="BusinessStrategyEvaluator",
    system_prompt="""
    Evaluate **business strategy and competitive positioning**:
    - **Industry Analysis**: Market trends, global expansion opportunities.
    - **Competitive Landscape**: Direct competitors, market share, differentiation.
    - **Strategic Growth Opportunities**: Mergers, acquisitions, R&D investment, sustainability.
    - Provide **long-term growth recommendations** and market dominance strategies.
    """,
    llm="gpt-4o",
)

aggregator_agent = TroveAgent(
    agent_name="ReportAggregator",
    system_prompt="""
    Generate a **rich, detailed 10-page business analysis report**:
    1️⃣ **Company Overview** - Market positioning, history, key milestones.
    2️⃣ **Financial Performance** - Revenue, profitability, debt trends over years.
    3️⃣ **Risk Assessment** - Market, regulatory, financial, operational risks.
    4️⃣ **Business Strategy Analysis** - Innovations, expansion, competition landscape.
    5️⃣ **Market & Industry Trends** - EV sector growth, economic trends.
    6️⃣ **Future Outlook & Recommendations** - Strategic directions, investment advice.
    7️⃣ **Data Insights & Visualization** - Charts, trends, and comparisons.
    """,
    llm="gpt-4o",
)

# **🔥 Initialize Mixture-of-Agents**
moa = TroveMOA(
    name="Trove-MOA-BusinessAnalysis",
    agents=[financial_agent, risk_agent, strategy_agent],
    layers=2,
    final_agent=aggregator_agent,
)

# **🏢 Example Execution for Tesla**
company_name = "Tesla"
result = moa.run(f"Generate a comprehensive business analysis report for {company_name}.")

print("\n📊 **Final Aggregated Report:**\n", result)
