import openai

class Agent:
    def __init__(self, agent_name, system_prompt, llm, max_loops=3, **kwargs):
        """
        A local implementation of an AI agent.

        Args:
            agent_name (str): The name of the agent.
            system_prompt (str): The prompt instructing the AI model.
            llm (AIModel): The language model instance (e.g., GPT-4).
            max_loops (int): Number of iterations to refine the response.
        """
        self.agent_name = agent_name
        self.system_prompt = system_prompt
        self.llm = llm
        self.max_loops = max_loops

    def run(self, user_query):
        """
        Runs the agent and generates a response.

        Args:
            user_query (str): The input question/query.

        Returns:
            str: The generated response.
        """
        full_prompt = f"{self.system_prompt}\nUser Query: {user_query}"

        print(f"\n🔍 DEBUG: Full Prompt Sent to OpenAI:\n{full_prompt}\n")

        try:
            response = self.llm.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": self.system_prompt},
                          {"role": "user", "content": user_query}],
                temperature=0.1,
                max_tokens=500
            )

            output = response.choices[0].message.content.strip()

            print(f"\n✅ DEBUG: Response Generated: {output}\n")
            return output

        except Exception as e:
            print(f"\n❌ ERROR: Failed to generate response: {e}")
            return None
