# Open-Source Multi-Agent Framework - Trove

## Overview
The **Trove Multi-Agent Framework** is a fully open-source, modular, and extensible AI framework designed for multi-agent collaboration. This framework enables seamless interaction between intelligent agents, equipping them with the ability to leverage tools, process real-world data, and automate complex decision-making across diverse domains such as **mobility, logistics, healthcare, finance, energy, research, cybersecurity, and industrial automation**.

Trove is envisioned as a **catalyst for accelerating AI innovation**, providing an open foundation for developing state-of-the-art autonomous agents that can assist in eliminating repetitive tasks, optimizing workflows, and augmenting human intelligence. By making **AI-driven automation more accessible**, Trove empowers researchers, developers, and enterprises to build intelligent agents that can **autonomously perform complex operations**, reducing cognitive load and driving efficiency.

## Why Trove?
In an era where AI adoption is increasing across industries, having an **open-source** and **community-driven** framework allows rapid experimentation, knowledge sharing, and the creation of highly specialized AI agents. Trove aims to:
- Democratize AI-driven automation by **lowering the barriers to entry**.
- Enable seamless **plug-and-play interactions** between AI agents and real-world systems.
- Provide a robust foundation to accelerate AI-driven innovation and **rapid prototyping of new autonomous workflows**.
- Serve as an ecosystem where researchers and developers **collaborate and enhance agent-based architectures**.

## Features
Trove is built with flexibility, scalability, and ease of integration in mind. Here are the key features:

### **1️⃣ Multi-Agent Collaboration & Autonomy**
- **Decentralized & Autonomous Agents**: Agents can operate independently or collaboratively, making distributed AI decision-making possible.
- **Cross-Agent Communication**: Support for inter-agent messaging, negotiation, and task delegation.
- **Hierarchical & Peer-to-Peer Coordination**: Agents can take on leadership roles or work in a decentralized manner.

### **2️⃣ Modular & Extensible Architecture**
- **Composable Agents**: Easily create agents with distinct capabilities by adding specialized tools and memory modules.
- **Pluggable Tooling**: Integrate external APIs, data pipelines, and ML models to enhance agent functionality.
- **Dynamic Workflow Execution**: Adapt agent behavior dynamically based on task requirements.

### **3️⃣ Intelligent Task Management & Workflow Automation**
- **Goal-Oriented Execution**: Agents break down high-level objectives into subtasks and execute them efficiently.
- **Context-Aware Processing**: Agents retain memory, learn from past interactions, and adapt to new inputs.
- **Human-in-the-Loop Interaction**: Support for human oversight and decision validation.

### **4️⃣ Advanced Memory & Knowledge Retention**
- **Long-Term & Short-Term Memory Modules**: Maintain contextual awareness across interactions.
- **RAG (Retrieval-Augmented Generation) Support**: Enable agents to retrieve and synthesize information from vast datasets.
- **Knowledge Graph Integration**: Connect structured and unstructured knowledge for better reasoning.

### **5️⃣ Data Processing & Analytics Capabilities**
- **Real-Time Data Ingestion**: Agents can process live data streams from IoT devices, databases, and APIs.
- **Multi-Modal Data Handling**: Process text, images, numerical data, and geospatial information.
- **Predictive & Prescriptive Analytics**: Leverage AI models for forecasting and intelligent decision-making.

### **6️⃣ Security, Privacy & Compliance**
- **End-to-End Encryption**: Secure agent communications and data storage.
- **Privacy-Preserving AI**: Implement federated learning and differential privacy techniques.
- **Access Control & Authentication**: Role-based permissions for enhanced security.

### **7️⃣ Open-Source Community & Customization**
- **Flexible Licensing**: MIT-licensed for unrestricted modification and use.
- **Active Developer Community**: Contribute to and extend the framework through community-led innovations.
- **Prebuilt Agent Templates**: Jumpstart development with ready-to-use agent blueprints.

## How Trove Accelerates Innovation
By reducing the technical barriers in developing **intelligent, autonomous systems**, Trove enables researchers and developers to focus on solving real-world problems rather than reinventing the underlying agent architecture. Some of the key ways it accelerates innovation include:
- **Reducing Development Time**: Prebuilt components and modular design help launch new agents faster.
- **Optimizing Industrial Processes**: Automate repetitive, manual decision-making in logistics, finance, and energy sectors.
- **Enabling AI-Powered Assistants**: Deploy domain-specific AI agents to handle knowledge-intensive tasks such as medical diagnosis, financial analysis, and cybersecurity monitoring.
- **Facilitating Open Research & Collaboration**: Encourages researchers to build and share improvements, benefiting the broader AI ecosystem.

## Future Roadmap
- **Integration with Large Language Models (LLMs)**: Expand capabilities for **agent reasoning and decision-making**.
- **Multi-Modal Processing**: Enhance support for **audio, video, and image recognition**.
- **Federated Learning & Edge AI**: Improve scalability for **distributed AI applications**.
- **Blockchain & Smart Contracts**: Enable **trustless agent collaboration** for finance and supply chain management.
- **Multi-Cloud Deployment**: Optimize for **cloud and edge-based execution**.

---
### 🚀 **Join the Community & Start Building the Future of Autonomous AI!**


## Getting Started
This section guides you through **cleaning the repository**, setting up the **right virtual environment**, and **ensuring dependencies** are installed.

### Step 1: **Clean the Repository (Optional, but Recommended)**
If you've cloned the repository before and want to reset:
```sh
rm -rf trove-agt
```
Then, re-clone it:
```sh
git clone https://github.com/hari8g/trove-agt.git
cd trove-agt
```

### Step 2: **Ensure You Are in the Right Virtual Environment**
Create a virtual environment (if not already created):
```sh
python3 -m venv venv
```
Activate the virtual environment:
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```
- **Windows**:
  ```sh
  venv\Scripts\activate
  ```

To verify the environment is activated:
```sh
type python  # Should return path to the virtual env
```

### Step 3: **Install Dependencies**
Ensure all dependencies are installed as per `requirements.txt`:
```sh
pip install -r requirements.txt
```

### Step 4: **Verify Installation**
Run the following to check if everything is installed correctly:
```sh
python -m pip list
```
Make sure all necessary libraries (like `openai`, `matplotlib`, `fpdf`, `dotenv`) are installed.

---
## Repository Structure

The project follows a structured approach:
```
 trove-agt/
 ├── agents_trove/           # Contains all agent definitions
 │   ├── trove_agent.py      # Main TroveAgent class (base for all agents)
 ├── tools_trove/            # Additional tools for agents
 │   ├── efficiency_tool.py  # A tool to calculate energy efficiency
 ├── data_trove/             # Stores structured data files
 │   ├── energy_data.json    # JSON dataset for energy analysis
 ├── scripts_trove/          # Scripts for running the framework
 │   ├── energy_assistant.py # Example use case (Energy Assistant)
 ├── env/                    # Environment configurations
 │   ├── .env                # Stores API keys & secrets (excluded from Git)
 ├── requirements.txt        # Lists dependencies
 ├── README.md               # Documentation
```
---
## Trove Architecture
### **Understanding `trove_agent.py` (Core of the Framework)**
The `trove_agent.py` file inside `agents_trove/` defines the **TroveAgent class**, which is the **foundation of the multi-agent system**. It acts as the base class from which specialized agents (like the Energy Assistant) inherit core functionalities.

### **Core Components of TroveAgent**
1. **Initialization (`__init__` method)**
   - Sets up the agent with key attributes such as:
     - `agent_name`: Unique identifier for the agent.
     - `system_prompt`: Defines the role and functionality of the agent.
     - `llm`: Defines the AI model the agent will use.
     - `autosave`: Determines if the agent should save states automatically.
     - `verbose`: Enables detailed logging for debugging.
   
2. **Memory Management**
   - Implements both **short-term** and **long-term memory**.
   - Memory storage allows agents to retain and retrieve past information for decision-making.
   
3. **Tool Integration**
   - Agents can register and utilize tools dynamically.
   - Example: The `calculate_efficiency` function in `tools_trove/efficiency_tool.py` is added to the agent as a tool.
   
4. **Task Execution (`run` method)**
   - Processes user inputs, interacts with tools, and generates AI-driven responses.
   - Enables multi-turn interactions between agents.
   
5. **State Management & Persistence**
   - Saves agent states in **JSON, YAML, and TOML formats**.
   - Can reload past states to maintain context across sessions.
   
6. **Dynamic Learning & Adaptation**
   - Can **ingest documents** and **learn from external sources**.
   - Enables advanced analysis, such as **retrieval-augmented generation (RAG)**.

### **Example Workflow of TroveAgent**
- When an agent (e.g., Energy Assistant) is instantiated:
  1. It loads **configuration** and **memory states**.
  2. It **retrieves energy data** from `data_trove/energy_data.json`.
  3. It processes user requests through **LLM-based analysis**.
  4. It executes relevant **tools**, such as efficiency calculation.
  5. It **generates reports** and saves outputs for further use.

---
## Example: Running the Energy Assistant
The **Energy Assistant** is an agent that analyzes energy consumption and generates efficiency reports.

### **Step 1: Setup API Keys**
Ensure your `.env` file inside the `env/` folder has your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

### **Step 2: Run the Energy Assistant**
Execute the script inside the `scripts_trove/` folder:
```sh
cd scripts_trove
python energy_assistant.py
```

### **Step 3: Expected Output**
- The script loads **energy data** from `data_trove/energy_data.json`
- It performs an **energy consumption analysis**
- It calculates **efficiency** using the efficiency tool
- Generates a **PDF report** with:
  - **Insights from AI** 📊
  - **Tabular Representation** 📝
  - **Graphs and Charts** 📈

### **Step 4: Locate the Report**
The PDF report is saved in the same folder as `energy_assistant.py`:
```
energy_report.pdf
```

---
## Contribution Guidelines
To contribute:
1. **Fork the repository**
2. **Create a new branch**:
   ```sh
   git checkout -b new-feature
   ```
3. **Make changes and commit**:
   ```sh
   git commit -m "Added new feature"
   ```
4. **Push to GitHub**:
   ```sh
   git push origin new-feature
   ```
5. **Create a Pull Request** 🚀

---
## License
This project is **open-source** and licensed under the **MIT License**.

---
### 🚀 **Start Exploring the Trove Multi-Agent Framework!**

