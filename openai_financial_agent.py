from models.agents.financial_agent import FinancialAgent

if __name__ == "__main__":
    # Initialize Financial Agent with OpenAI
    agent = FinancialAgent(model_type="openai")

    # Example Query
    query = "What are the best stocks to invest in 2024?"

    # Get AI Response
    response = agent.analyze_financial_query(query)

    print("✅ AI Response:")
    print(response)
