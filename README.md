# 🚀 Trove Dynamic Agent - AI-Powered Task Execution Framework

## 🔹 Introduction

Trove Dynamic Agent is an AI-powered framework that allows users to create domain-specific AI agents capable of performing various tasks dynamically. This system enables real-time AI assistance across different domains by providing structured, well-defined responses based on a **Meta-System Prompt Framework**.

With **Trove Dynamic Agent**, users can:
- ✅ **Create AI Agents on the fly** for **finance, healthcare, education, and more**.
- ✅ **Define tasks dynamically** by specifying **what the agent should do**.
- ✅ **Interact with AI agents in a human-like, professional manner**.
- ✅ **Get structured, clear, and well-explained responses**.

---

## 🚀 Features

- ✔️ **Dynamic AI Agent Creation**: Instantly generates agents based on user-defined domains and tasks.
- ✔️ **Meta-System Prompting**: Uses structured AI prompt engineering for precise task execution.
- ✔️ **OpenAI GPT-4o Support**: Leverages powerful **GPT-4o** for highly accurate AI responses.
- ✔️ **Customizable Responses**: Format responses in a **clear, readable, structured way**.
- ✔️ **Fully Extensible**: Developers can create new agents for different use cases.
- ✔️ **No Dependency on External Frameworks**: Uses a **local `Agent` implementation**, replacing `swarms`.

---

## 📌 Installation Guide

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/trove-agt.git
cd trove-agt
```

### **2️⃣ Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up OpenAI API Key**
Create a `.env` file in the root directory and add your OpenAI API key:
```bash
touch .env
echo "OPENAI_API_KEY=your_api_key_here" >> .env
```
Or manually edit `.env`:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

### **5️⃣ Verify Installation**
```bash
python -c "import openai; print(openai.__version__)"
```
If OpenAI is installed, it should print a version number.

---

## 📌 Usage Guide

### **1️⃣ Run a Dynamic Agent**
```bash
python scripts/run_dynamic_agent.py --domain financial --task "Analyze stock market trends for 2024 and provide investment insights." --query "What are the top 3 stocks for 2024?"
```

### **2️⃣ Example Output**
```
🐜 **AI Response**
══════════════════════════════════════
📊 **Investment Analysis for 2024:**
1️⃣ **Apple (AAPL)** - Growth: 12% YoY, driven by AI and cloud expansion.
2️⃣ **Tesla (TSLA)** - Growth: 15% YoY, strong EV market share increase.
3️⃣ **NVIDIA (NVDA)** - Growth: 18% YoY, AI chip dominance.
✅ **Recommendation:** Diversify across stable and growth stocks.
══════════════════════════════════════
```

---

## 📌 Extending the Agent Framework

### **Adding a New AI Agent**
Modify: **`models/agents/dynamic_agent.py`**
```python
elif self.domain == "legal":
    self.system_prompt += "\nAgent Role: Legal Advisor\nObjective: Provide legal insights."
```
Run it:
```bash
python scripts/run_dynamic_agent.py --domain legal --task "Analyze tech law trends." --query "What are the major AI regulations in 2024?"
```

---

## 📌 Contributing

🔹 **We welcome contributions!**
1. **Fork the repo** and create a new branch.
2. **Make your changes** and test thoroughly.
3. **Submit a pull request (PR).**
4. **We will review & merge your changes!** 🚀

---

## 📌 Troubleshooting

### **Common Issues & Fixes**
- ❌ **Agent doesn’t return a response?**
  - ✅ Ensure your OpenAI API key is valid and you have enough credits.
- ❌ **Installation issues?**
  - ✅ Run `pip install -r requirements.txt` again and ensure dependencies are installed.
- ❌ **Need help?**
  - ✅ Open an issue on GitHub or reach out to us.

---

## 📌 License
This project is open-source under the **MIT License**. Feel free to use, modify, and contribute! 🚀

---

## 🎯 Now You’re Ready!
🎉 **Congratulations!** You now have a **fully functional AI-powered agent** that dynamically adapts to user needs.

🚀 **Start building with Trove Dynamic Agent today!** 🚀

