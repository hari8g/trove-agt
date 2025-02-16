import openai
import os
from utils.config import OPENAI_API_KEY

class GPTModel:
    def __init__(self, model_name="gpt-4o-mini", temperature=0.1):
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.model_name = model_name
        self.temperature = temperature

    def generate_response(self, prompt):
        try:
            response = self.client.Completion.create(
                model=self.model_name,
                prompt=prompt,
                temperature=self.temperature
            )
            return response['choices'][0]['text'].strip()
        except Exception as e:
            print(f"❌ Error generating response: {e}")
            return None
