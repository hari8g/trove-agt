class CustomModel:
    def __init__(self):
        self.system_prompt = "You are an AI assistant providing helpful answers."

    def generate_response(self, query):
        return f"{self.system_prompt} Here is your answer to: '{query}'"
