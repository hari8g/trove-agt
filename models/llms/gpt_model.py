import os
import openai
from transformers import pipeline
from utils.config import CONFIG

class AIModel:
    def __init__(self, model_type="openai"):
        self.model_type = model_type

        if self.model_type == "openai":
            self.api_key = CONFIG.get("openai")["api_key"]
            self.client = openai.OpenAI(api_key=self.api_key)
        elif self.model_type == "huggingface":
            self.model_name = CONFIG.get("huggingface")["model_name"]
            self.generator = pipeline("text-generation", model=self.model_name)
        else:
            raise ValueError("Unsupported model type!")

    def generate_response(self, prompt):
        if self.model_type == "openai":
            response = self.client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a financial assistant."},{"role": "user", "content": prompt}],
    temperature=0.1
            )
            return response.choices[0].message.content.strip()
        elif self.model_type == "huggingface":
            return self.generator(prompt, max_length=50)[0]["generated_text"]
        else:
            return "❌ Invalid model type"
