import importlib

class AgentRegistry:
    _agents = {}

    @classmethod
    def register(cls, name, agent_path):
        cls._agents[name] = agent_path

    @classmethod
    def get_agent(cls, name):
        if name not in cls._agents:
            raise ValueError(f"Agent '{name}' not found.")
        module_name, class_name = cls._agents[name].rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)()

# Register agents
AgentRegistry.register("financial", "models.agents.financial_agent.FinancialAgent")
