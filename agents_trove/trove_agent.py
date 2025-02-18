import os
import json
import yaml
import toml
import logging
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TroveAgent:
    """
    TroveAgent: A customizable AI agent capable of executing tasks, managing memory, interacting with tools, and saving/loading states.
    This class provides extensive customization and supports various integrations for enhanced functionality.
    """
    
    def __init__(self,
                 agent_name: str = "DefaultAgent",
                 system_prompt: str = "Default system prompt.",
                 llm: str = "OpenAIChat",
                 max_loops: int = 1,
                 autosave: bool = False,
                 dashboard: bool = False,
                 verbose: bool = False,
                 dynamic_temperature_enabled: bool = False,
                 saved_state_path: str = "agent_state.json",
                 user_name: str = "default_user",
                 retry_attempts: int = 1,
                 context_length: int = 200000,
                 return_step_meta: bool = False,
                 output_type: str = "string"):
        """
        Initializes the TroveAgent with customizable parameters.
        
        :param agent_name: Name of the agent.
        :param system_prompt: The system prompt that defines the agent's behavior.
        :param llm: The language model used for processing.
        :param max_loops: Maximum iterations for task execution.
        :param autosave: Enables automatic state saving.
        :param dashboard: Enables dashboard logging.
        :param verbose: Controls verbosity.
        :param dynamic_temperature_enabled: Enables dynamic temperature adjustments for LLM.
        :param saved_state_path: File path for saving agent state.
        :param user_name: User associated with the agent.
        :param retry_attempts: Number of retries for failed tasks.
        :param context_length: Maximum length of input context.
        :param return_step_meta: Enables metadata return for steps.
        :param output_type: Format of the agent output (e.g., string, json).
        """
        self.agent_name = agent_name
        self.system_prompt = system_prompt
        self.llm = llm
        self.max_loops = max_loops
        self.autosave = autosave
        self.dashboard = dashboard
        self.verbose = verbose
        self.dynamic_temperature_enabled = dynamic_temperature_enabled
        self.saved_state_path = saved_state_path
        self.user_name = user_name
        self.retry_attempts = retry_attempts
        self.context_length = context_length
        self.return_step_meta = return_step_meta
        self.output_type = output_type
        self.short_term_memory: List[str] = []
        self.long_term_memory: Dict[str, Any] = {}
        self.tools: Dict[str, Any] = {}

        logging.info(f"Agent {self.agent_name} initialized with LLM: {self.llm}")
    
    def run(self, task: str) -> str:
        """
        Executes a task with memory and tool interaction.
        
        :param task: The task description.
        :return: Task execution result.
        """
        logging.info(f"{self.agent_name} executing task: {task}")
        self.short_term_memory.append(task)
        result = self._process_task(task)
        return result

    def _process_task(self, task: str) -> str:
        """Internal method for processing a given task."""
        if "use_tool" in task:
            tool_name = task.split(" ")[1]
            return self.execute_tool(tool_name, {})
        return f"Task '{task}' completed by {self.agent_name}"

    def add_tool(self, tool_name: str, function: Any):
        """Registers a tool for the agent."""
        self.tools[tool_name] = function
        logging.info(f"Tool {tool_name} added to {self.agent_name}")
    
    def execute_tool(self, tool_name: str, params: Dict[str, Any]) -> str:
        """Executes a tool if it exists."""
        if tool_name in self.tools:
            return self.tools[tool_name](**params)
        return f"Tool {tool_name} not found"

    def save_state(self):
        """Saves the agent's state to a JSON file."""
        state = self.to_dict()
        with open(self.saved_state_path, "w") as file:
            json.dump(state, file)
        logging.info(f"State saved to {self.saved_state_path}")
    
    def load_state(self):
        """Loads the agent's state from a JSON file."""
        with open(self.saved_state_path, "r") as file:
            state = json.load(file)
        self.__dict__.update(state)
        logging.info(f"State loaded from {self.saved_state_path}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts agent attributes to a dictionary."""
        return self.__dict__

    def to_toml(self) -> str:
        """Converts agent attributes to TOML format."""
        return toml.dumps(self.to_dict())

    def model_dump_json(self):
        """Dumps agent attributes to a JSON file."""
        with open(f"{self.agent_name}.json", "w") as file:
            json.dump(self.to_dict(), file)
        logging.info(f"Model state saved as JSON: {self.agent_name}.json")

    def model_dump_yaml(self):
        """Dumps agent attributes to a YAML file."""
        with open(f"{self.agent_name}.yaml", "w") as file:
            yaml.dump(self.to_dict(), file)
        logging.info(f"Model state saved as YAML: {self.agent_name}.yaml")

    def ingest_docs(self, docs: List[str]):
        """Ingests documents into the agent's long-term memory."""
        self.long_term_memory["documents"] = docs
        logging.info("Documents ingested into memory.")

    def receive_message(self, message: str):
        """Handles incoming messages."""
        logging.info(f"Message received: {message}")
        return f"Processed message: {message}"

    def send_agent_message(self, recipient: str, message: str):
        """Sends a message from the agent."""
        return f"Sent message to {recipient}: {message}"
    
    def print_dashboard(self):
        """Prints dashboard if enabled."""
        if self.dashboard:
            logging.info(f"Agent: {self.agent_name} | LLM: {self.llm} | Memory size: {len(self.long_term_memory)}")
    
if __name__ == "__main__":
    agent = TroveAgent()
    agent.add_tool("example_tool", lambda: "Example tool executed")
    print(agent.run("Test Task"))
    print(agent.execute_tool("example_tool", {}))
    agent.save_state()
    agent.load_state()
    agent.model_dump_json()
    agent.model_dump_yaml()

