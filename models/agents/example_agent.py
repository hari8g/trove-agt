from models.llms.custom_model import CustomModel

class ExampleAgent:
    def __init__(self):
        self.llm = CustomModel()

    def ask(self, query):
        return self.llm.generate_response(query)
