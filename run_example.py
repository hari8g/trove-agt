from models.agents.example_agent import ExampleAgent

if __name__ == "__main__":
    agent = ExampleAgent()
    
    # Example Query
    query = "What is the future of AI?"
    
    # Get Response
    response = agent.ask(query)
    
    print("✅ AI Response:")
    print(response)
