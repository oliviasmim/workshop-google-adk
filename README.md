# TDC CrewAI Workshop

This repository contains code examples and resources for the TDC Summit AI 2025 workshop. The goal is to demonstrate how to build and run multi-agent systems using CrewAI, LangChain, and Streamlit. Each directory in this repository contains a progressively more complex example, starting from a simple agent and culminating in a fully interactive Streamlit interface.

---

## Installation Details

### Requirements

- **Python**: 3.12 or higher
- **Pip**: Latest version (ensure it's updated)
- **Virtual Environment**: Recommended for dependency isolation

### Dependencies

The project uses the following libraries:

- `openai`
- `crewai`
- `crewai[tools]`
- `langchain`
- `streamlit`
- `python-dotenv`
- `chromadb`
- `markdown`
- `langchain_community`
- `langchain-chroma`
- `numpy`

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/oliviasmim/tdc-crewai-workshop.git
cd tdc-crewai-workshop
```

### 2. Set Up a Virtual Environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a .env file in the root directory with the following content:

```env
OPENAI_API_KEY="your-openai-api-key"
SERPER_API_KEY="your-serper-api-key"
```

Replace `your-openai-api-key` and `your-serper-api-key` with your actual API keys.

---

## Directory Walkthrough

### 1. 1-hello-world-crew

This directory contains the simplest example of using CrewAI. It demonstrates how to set up a single agent and run a basic task.

#### Key Files:

- main.py: The entry point for the example. It initializes a single agent and assigns it a simple task.

#### Steps to Run:

1. Navigate to the directory:
   ```bash
   cd 1-hello-world-crew
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Output:
   - The agent will greet the user with a welcome message.

---

### 2. 2-multi-agent-crew

This directory demonstrates a multi-agent system where agents collaborate to complete tasks. It introduces the concept of task dependencies and agent collaboration.

#### Key Files:

- `multi-crew.ipynb`: A Jupyter Notebook that walks through the multi-agent workflow.
- sample_code.tsx: Example code for integrating multi-agent systems into a frontend.

#### Steps to Run:

1. Navigate to the directory:
   ```bash
   cd 2-multi-agent-crew
   ```
2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook multi-crew.ipynb
   ```
   Or simple use the VSCode extension to open the notebook.
3. Follow the instructions in the notebook to execute the multi-agent workflow.

---

### 3. 3-crew-with-tools

This directory integrates tools like search engines and web scraping into the CrewAI workflow. It demonstrates how agents can use external tools to enhance their capabilities.

#### Key Files:

- main.py: The entry point for the example. It initializes agents and tasks with tool integration.
- agents.py: Defines the agents and their roles.
- tasks.py: Defines the tasks and their descriptions.

#### Steps to Run:

1. Navigate to the directory:
   ```bash
   cd 3-crew-with-tools
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. Output:
   - The agents will use tools to gather and analyze data for the specified theme.

---

### 4. 4-streamlit-interface

This directory provides a Streamlit-based user interface for interacting with the CrewAI system. It allows users to input a technology theme and view the research results in real-time.

#### Key Files:

- `app.py`: The main Streamlit app file.
- `research_engine.py`: Handles the research workflow.
- agents.py: Defines the agents used in the workflow.
- tasks.py: Defines the tasks assigned to the agents.

#### Steps to Run:

1. Navigate to the directory:
   ```bash
   cd 4-streamlit-interface
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser (Streamlit will provide a local URL).
4. Enter a technology theme and start the research process.

---

## Additional Notes

- **Debugging**: If you encounter issues, check the .env file for correct API keys and ensure all dependencies are installed.
- **API Limits**: Be mindful of API usage limits for OpenAI and Serper.
- **Customization**: Modify the agents and tasks in the agents.py and tasks.py files to experiment with different workflows.

---
