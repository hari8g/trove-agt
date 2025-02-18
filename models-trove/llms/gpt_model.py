import os
import openai
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

class AIModel:
    def __init__(self, model_type="openai"):
        """
        Initializes an AI model instance.
        """
        self.model_type = model_type
        self.api_key = os.getenv("OPENAI_API_KEY")

        # ✅ Force API key check
        if not self.api_key:
            raise ValueError("❌ ERROR: OPENAI_API_KEY is missing. Ensure it's set in .env or environment variables.")

        print(f"🔍 DEBUG: Using OpenAI API Key: {self.api_key[:5]}**********")  # ✅ Print first 5 characters for verification

        if model_type == "openai":
            self.client = openai.OpenAI(api_key=self.api_key)  # ✅ Fix client initialization

    def generate_response(self, user_message):
        """
        Generates a response using OpenAI GPT chat model.
        """
        print(f"\n🔍 DEBUG: Sending Prompt to LLM: {user_message}")

        try:
            response = self.client.chat.completions.create(  
                model="gpt-4o",  
                messages=[{"role": "user", "content": user_message}],
                temperature=0.1,
                max_tokens=500
            )

            output = response.choices[0].message.content.strip()
            print(f"\n✅ DEBUG: LLM Output Received: {output}")  # ✅ Debug print
            return output

        except Exception as e:
            print(f"\n❌ ERROR: Failed to get LLM response: {e}")
            return None
