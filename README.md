# 🚀 Trove AI Agent Framework

Trove is a customizable AI Agent framework that allows users to build and integrate AI agents powered by OpenAI's GPT models and Hugging Face transformers. It simplifies the development of intelligent agents for various tasks.

---

## 🌟 Features

- **Customizable Agents:** Build agents for financial analysis, data processing, and more.
- **Multiple LLMs Support:** Integrates OpenAI's GPT models and Hugging Face models.
- **Modular Architecture:** Easily add new models and agents.

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- `virtualenv` (Optional, for virtual environments)

### Clone the Repository

```bash
git clone https://github.com/hari8g/trove-agt.git
cd trove-agt
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

### Configure OpenAI API Key

1. Create a `.env` file in the project root:

```bash
nano .env
```

Add your OpenAI API key:

```
OPENAI_API_KEY=your-secret-api-key
```

### Run the Financial Agent Example

```bash
python openai_financial_agent.py
```

**Expected Output:**

```
✅ AI Response:
The best stocks to invest in 2024 depend on market trends, economic indicators, and industry performance...
```

---

## 🧪 Examples

### Example 1: Running the Financial Agent

```bash
python openai_financial_agent.py
```

**Example Query:**

```python
query = "What are the best investment opportunities in India?"
response = agent.analyze_financial_query(query)
print(response)
```

**Example Output:**

```
✅ AI Response:
Investing in technology and renewable energy sectors in India shows promising growth for 2024.
```

---

### Example 2: Running a Custom Agent

To build and run a custom agent:

1. Create a new agent in `models/agents/custom_agent.py`.
2. Customize your logic.
3. Run the script.

---

## 📂 Project Structure

```
trove-agt/
├── models/
│   ├── agents/
│   │   └── financial_agent.py
│   └── llms/
│       └── gpt_model.py
├── utils/
│   └── config.py
├── .env
├── requirements.txt
├── README.md
├── openai_financial_agent.py
└── src/
    └── run_example.py
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📧 Contact

If you have any questions or feedback, feel free to reach out:

- **Email:** hariprasad.gs88@gmail.com
- **GitHub Issues:** [Open an issue](https://github.com/hari8g/trove-agt/issues)

---

## ⭐️ Star the Repository

If you find this project useful, please star it on GitHub! 🌟

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more information.
