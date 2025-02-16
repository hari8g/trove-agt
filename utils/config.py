import yaml
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self, key):
        if key == "openai":
            self.config[key]["api_key"] = os.getenv("OPENAI_API_KEY")  # Load from .env
        return self.config.get(key)

CONFIG = Config()

