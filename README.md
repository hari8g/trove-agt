# 🚀 Trove Dynamic Agent - AI-Powered Task Execution Framework

## 📌 Introduction

Trove Dynamic Agent is an **AI-powered framework** that allows users to create **domain-specific AI agents** capable of performing various tasks dynamically. This system enables real-time AI assistance across different domains by providing structured, well-defined responses based on a **Meta-System Prompt Framework**.

### **Key Capabilities:**
✅ **Create AI Agents on the fly** for **finance, healthcare, education, and more**.
✅ **Define tasks dynamically** by specifying **what the agent should do**.
✅ **Interact with AI agents in a human-like, professional manner**.
✅ **Get structured, clear, and well-explained responses**.

---

## 🚀 Features

✔️ **Dynamic AI Agent Creation**: Instantly generates agents based on user-defined domains and tasks.
✔️ **Meta-System Prompting**: Uses structured AI prompt engineering for precise task execution.
✔️ **OpenAI GPT-4o Support**: Leverages powerful **GPT-4o** for highly accurate AI responses.
✔️ **Customizable Responses**: Format responses in a **clear, readable, structured way**.
✔️ **Fully Extensible**: Developers can create new agents for different use cases.
✔️ **No Dependency on External Frameworks**: Uses a **local `Agent` implementation**, replacing `swarms`.

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
python scripts/run_dynamic_agent.py --domain financial --task "Analyze stock market trends for 2025 in India and provide investment insights." --query "What are the top 3 stocks to buy in India in 2025?"
```

### **2️⃣ Example Output**
📜 **AI Response**
═══════════════════════════════════════════════
To identify the top stocks to buy in India in 2025, we need to consider several
factors, including economic trends, sector performance, and company
fundamentals. While I can't predict specific stock prices, I can provide
insights into sectors and companies that may present growth opportunities based
on current trends and projections.

### **1️⃣ Information Technology (IT) Sector**
- **Company to Watch: Tata Consultancy Services (TCS)**  
  - **Rationale**: The IT sector in India has been a consistent performer, driven by
global demand for digital transformation services. TCS, as a leader in this
space, benefits from its strong client base, robust financials, and continuous
innovation in AI and cloud services.  
  - **Risk Assessment**: Currency fluctuations and global economic slowdowns could impact revenue. However, the
sector's resilience and adaptability to new technologies mitigate some risks.

### **2️⃣ Renewable Energy Sector**
- **Company to Watch: Adani Green Energy**  
  - **Rationale**: With India's commitment to increasing its renewable energy
capacity, companies like Adani Green Energy are well-positioned to benefit from
government incentives and growing demand for sustainable energy solutions.  
  - **Risk Assessment**: Regulatory changes and project execution risks are potential challenges. However, the
long-term growth trajectory remains positive due to the global shift towards clean energy.

### **3️⃣ Consumer Goods Sector**
- **Company to Watch: Hindustan Unilever Limited (HUL)**  
  - **Rationale**: As a leader in the FMCG sector, HUL is poised to benefit from India's growing middle
class and increasing consumer spending. The company's strong brand portfolio and
distribution network provide a competitive edge.  
  - **Risk Assessment**: Inflationary pressures and changes in consumer preferences could impact margins.
Nonetheless, HUL's ability to adapt its product offerings and pricing strategies
helps mitigate these risks.

### **Actionable Insights for Investors:**
- **Diversification**: Consider diversifying across these sectors to balance potential risks and rewards.
- **Long-term Perspective**: Focus on long-term growth potential rather than short-term market fluctuations.
- **Stay Informed**: Keep abreast of economic policies, technological advancements, and sector-specific developments that could impact these companies.
═══════════════════════════════════════════════

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
python scripts/run_dynamic_agent.py --domain legal --task "Analyze tech law trends." --query "What are the major AI regulations in 2025?"
```

---

## 📌 Contributing

🔹 **We welcome contributions!**
1️⃣ **Fork the repo** and create a new branch.
2️⃣ **Make your changes** and test thoroughly.
3️⃣ **Submit a pull request (PR).**
4️⃣ **We will review & merge your changes!** 🚀

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

