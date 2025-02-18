import textwrap
from models.agents.agent import Agent  
from prompts.meta_system_prompt import META_SYSTEM_PROMPT  

class DynamicAgent:
    def __init__(self, domain, task_description, llm):
        """
        Initializes a dynamic AI agent with a domain and task description.
        """
        self.domain = domain
        self.task_description = task_description
        self.llm = llm  
        self.system_prompt = self._generate_system_prompt()

    def _generate_system_prompt(self):
        """
        Uses the Meta-System Prompt Framework to generate a structured task prompt.
        """
        structured_prompt = META_SYSTEM_PROMPT.format(
            domain=self.domain, task_description=self.task_description
        )

        print("\n🔍 Generating System Prompt for Agent...")
        print(f"📌 SYSTEM PROMPT:\n{structured_prompt}\n")

        try:
            response = self.llm.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": structured_prompt}],
                temperature=0.1,
                max_tokens=500
            )

            system_prompt_generated = response.choices[0].message.content.strip()

            print("\n✅ System Prompt Generated Successfully!")
            print(f"🔹 FINAL SYSTEM PROMPT:\n{system_prompt_generated}\n")

            return system_prompt_generated

        except Exception as e:
            print(f"\n❌ ERROR: Failed to generate system prompt: {e}")
            return None

    def execute(self, user_query):
        """
        Executes the agent using the generated system prompt and a user query.
        """
        print(f"\n🔍 Running Agent on Query: {user_query}")
        print(f"\n🔍 DEBUG: SYSTEM PROMPT BEING USED:\n{self.system_prompt}")

        agent = Agent(
            agent_name=f"{self.domain}-Agent",
            system_prompt=self.system_prompt,
            llm=self.llm,
            max_loops=5
        )

        print("\n🚀 Running Agent...")

        try:
            output = agent.run(user_query)  

            if output:
                print("\n✅ DEBUG: Agent Response Generated!")
                self._print_nice_output(output)  # ✅ Nicely formatted output
            else:
                print("\n⚠️ DEBUG: Agent did NOT generate a response!")

            print(f"\n🔍 DEBUG: Raw Output from Agent.run():\n{output}")  

        except Exception as e:
            print(f"\n❌ ERROR: {e}")

        return output

    def _print_nice_output(self, response):
        """
        Formats and prints the response in a clean, readable format.
        """
        print("\n📜 **AI Response**")
        print("═══════════════════════════════════════════════")
        formatted_response = textwrap.fill(response, width=80)  # ✅ Wraps long text
        print(formatted_response)
        print("═══════════════════════════════════════════════\n")
