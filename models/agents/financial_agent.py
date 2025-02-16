from models.llms.gpt_model import AIModel

class FinancialAgent:
    def __init__(self, model_type="openai"):
        self.llm = AIModel(model_type=model_type)
        self.system_prompt = "Analyze financial situations and provide investment advice..."

    def analyze_financial_query(self, query):
        prompt = f"{self.system_prompt}\nUser Query: {query}"
        return self.llm.generate_response(prompt)
