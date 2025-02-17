# 🚀 Trove Dynamic Agent - AI-Powered Task Execution Framework

## **🔹 Introduction**
Trove Dynamic Agent is an AI-powered framework that allows users to create domain-specific AI agents capable of performing various tasks dynamically.  
This system enables **real-time AI assistance** across different domains by providing structured, well-defined responses based on a **Meta-System Prompt Framework**.

With **Trove Dynamic Agent**, users can:
✅ **Create AI Agents on the fly** for **finance, healthcare, education, and more**.  
✅ **Define tasks dynamically** by specifying **what the agent should do**.  
✅ **Interact with AI agents in a human-like, professional manner**.  
✅ **Get structured, clear, and well-explained responses**.  

---

## **🚀 Features**
✔️ **Dynamic AI Agent Creation**: Instantly generates agents based on user-defined domains and tasks.  
✔️ **Meta-System Prompting**: Uses structured AI prompt engineering for precise task execution.  
✔️ **OpenAI GPT-4o Support**: Leverages powerful **GPT-4o** for highly accurate AI responses.  
✔️ **Customizable Responses**: Format responses in a **clear, readable, structured way**.  
✔️ **Fully Extensible**: Developers can create new agents for different use cases.  
✔️ **No Dependency on External Frameworks**: Uses a **local `Agent` implementation**, replacing `swarms`.  

---

## **📌 Installation Guide**
### **1️⃣ Clone the Repository**
First, clone the repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/trove-agt.git
cd trove-agt

2️⃣ Set Up Virtual Environment
Create and activate a virtual environment to manage dependencies:

python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Dependencies
Install the required dependencies using requirements.txt:

pip install -r requirements.txt

4️⃣ Set Up OpenAI API Key
Create a .env file in the root directory and add your OpenAI API key:

touch .env
echo "OPENAI_API_KEY=your_api_key_here" >> .env

Or manually edit .env:

OPENAI_API_KEY=your_api_key_here

5️⃣ Verify Installation
Ensure that everything is installed correctly by running:

python -c "import openai; print(openai.__version__)"

If OpenAI is installed, it should print a version number.

📌 Usage Guide

1️⃣ Run a Dynamic Agent
To create and run a custom AI agent, use the following command:

python scripts/run_dynamic_agent.py --domain financial --task "Analyze stock market trends for 2024 and provide investment insights." --query "What are the top 3 stocks for 2024?"

2️⃣ Example Output
📜 **AI Response**
═══════════════════════════════════════════════
📊 **Investment Analysis for 2024:**
1️⃣ **Apple (AAPL)** - Growth: 12% YoY, driven by AI and cloud expansion.
2️⃣ **Tesla (TSLA)** - Growth: 15% YoY, strong EV market share increase.
3️⃣ **NVIDIA (NVDA)** - Growth: 18% YoY, AI chip dominance.
✅ **Recommendation:** Diversify across stable and growth stocks.
═══════════════════════════════════════════════

3️⃣ Customizing the AI Agent
Modify the command by changing:

--domain → Specify different industries, e.g., healthcare, education, etc.
--task → Define a custom AI task.
--query → Ask a specific question.
Example for Healthcare AI Agent:

python scripts/run_dynamic_agent.py --domain healthcare --task "Analyze medical research trends for 2024." --query "What are the latest breakthroughs in cancer treatment?"

🔹 How Trove Dynamic Agent Works

1️⃣ Meta-System Prompt Framework
The agent relies on a Meta-System Prompt, which provides: ✅ Domain Context (Finance, Healthcare, Education, etc.)
✅ Task Specifications (Investment analysis, Medical research, etc.)
✅ Structured Output Expectations (Clear, professional responses)

2️⃣ OpenAI GPT-4o Integration
The agent interacts with GPT-4o, a powerful AI language model, to generate detailed, insightful responses.

3️⃣ Dynamic AI Task Execution
Users can dynamically generate AI agents that specialize in different areas and execute specific tasks in real-time.

📌 Extending the Agent Framework

1️⃣ Adding a New AI Agent
To create a new agent (e.g., Legal AI Agent), modify: 📌 models/agents/dynamic_agent.py

# Add support for legal agents
elif self.domain == "legal":
    self.system_prompt += "\nAgent Role: Legal Advisor\nObjective: Provide legal insights."
Run it:

python scripts/run_dynamic_agent.py --domain legal --task "Analyze tech law trends." --query "What are the major AI regulations in 2024?"

📌 Contributing

🔹 We welcome contributions!
To contribute, follow these steps: 1️⃣ Fork the repo and create a new branch.
2️⃣ Make your changes and test thoroughly.
3️⃣ Submit a pull request (PR).
4️⃣ We will review & merge your changes! 🚀

📌 Troubleshooting

Common Issues & Fixes
❌ Agent doesn’t return a response?
✅ Ensure your OpenAI API key is valid and you have enough credits.

❌ Installation issues?
✅ Run pip install -r requirements.txt again and ensure dependencies are installed.

❌ Need help?
✅ Open an issue on GitHub or reach out to us.

📌 Future Enhancements

🚀 Upcoming Features

🔹 Multi-Agent Collaboration: Agents working together on complex tasks.
🔹 Memory Integration: Agents that remember past queries.
🔹 Advanced Formatting: AI-generated reports in Markdown, JSON, or PDF.
📌 License

This project is open-source under the MIT License.
Feel free to use, modify, and contribute! 🚀

🎯 Now You’re Ready!
🎉 Congratulations! You now have a fully functional AI-powered agent that dynamically adapts to user needs.

🚀 Start building with Trove Dynamic Agent today! 🚀
