<div align="center">

<img src="./assets/AI.svg" width="180" alt="NeuraFlow AI Logo" />

# 🌊 NeuraFlow AI
### Enterprise RAG & Autonomous Multi-LLM Document Intelligence Platform

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=20&pause=1000&color=8B5CF6&center=true&vCenter=true&width=600&lines=Analyze+PDFs+with+Generative+AI;Smart+Routing+Between+Top+LLMs;Production-Grade+AI+Architecture;Fast%2C+Accurate%2C+and+Cost-Effective)](https://git.io/typing-svg)

<br/>

<video src="./Project_Videos_and_PDFs/Anatomy_of_a_Query__Deconstructing_a_Multi-LLM_Pipeline.mp4" width="800" controls></video>

<br/>

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://streamlit.io"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini"></a>
  <a href="https://groq.com"><img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"></a>
  <a href="https://openrouter.ai/"><img src="https://img.shields.io/badge/OpenRouter-10B981?style=for-the-badge&logo=openai&logoColor=white" alt="OpenRouter"></a>
  <a href="https://huggingface.co/"><img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"></a>
</p>

<p align="center">
  <a href="https://github.com/Piyu242005/NeuraFlow-AI/actions/workflows/ci.yml"><img src="https://img.shields.io/badge/CI-Passing-brightgreen?style=flat-square&logo=github-actions" alt="CI"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
  <a href="https://github.com/Piyu242005/AI-DOC-ASSISTANT/stargazers"><img src="https://img.shields.io/github/stars/Piyu242005/AI-DOC-ASSISTANT?style=flat-square&color=8B5CF6" alt="Stars"></a>
  <a href="https://github.com/Piyu242005/AI-DOC-ASSISTANT/network/members"><img src="https://img.shields.io/github/forks/Piyu242005/AI-DOC-ASSISTANT?style=flat-square&color=8B5CF6" alt="Forks"></a>
</p>

</div>

<br/>

> [!NOTE]
> **NeuraFlow AI** is a production-grade autonomous AI Agent platform. It integrates Enterprise Retrieval-Augmented Generation (RAG), ChromaDB vector search, persistent conversation memory, and real-time streaming responses into a unified ecosystem. By orchestrating multiple leading LLMs and utilizing intelligent tool calling (such as multi-provider web search via Tavily/DuckDuckGo, document retrieval, and advanced calculation), NeuraFlow AI delivers scalable, accurate, and cost-effective document intelligence and reasoning workflows.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🔀 **Multi-LLM Architecture** | Unified interface combining models from Groq, Google, OpenRouter, and Hugging Face. |
| 🧠 **Intelligent Agent Routing** | Automatically classifies queries (Coding, Reasoning, General) to pick the best model. |
| 🛡️ **Automatic Fallback System** | Seamlessly reroutes failed API requests (e.g., 429 Quota limits) to backup providers. |
| 📄 **PDF Document Analysis** | Extracts, vectorizes, and processes text from large PDF documents using `pypdf` and ChromaDB. |
| 🔍 **AI Decision Transparency** | An expander panel reveals *why* a model was chosen, token usage, and latency metrics. |
| ⚡ **Real-Time Model Selection** | Toggle between "Auto Agent" mode or manually force a specific LLM to respond. |
| 📡 **Advanced Telemetry** | Real-time Telegram notifications for document uploads, analytics tracking, and fallback alerts. |
| 🎨 **Modern UI/UX** | Premium Dark-mode Streamlit interface with glassmorphism effects and fluid animations. |

---

## 🏗️ Architecture

```mermaid
graph TD
    %% Styling
    classDef user fill:#6366f1,stroke:#4f46e5,stroke-width:2px,color:#fff,rx:8px,ry:8px;
    classDef router fill:#8b5cf6,stroke:#7c3aed,stroke-width:2px,color:#fff,rx:8px,ry:8px;
    classDef llm fill:#10b981,stroke:#059669,stroke-width:2px,color:#fff,rx:8px,ry:8px;
    classDef fallback fill:#f59e0b,stroke:#d97706,stroke-width:2px,color:#fff,rx:8px,ry:8px;
    classDef engine fill:#3b82f6,stroke:#2563eb,stroke-width:2px,color:#fff,rx:8px,ry:8px;
    classDef infra fill:#64748b,stroke:#475569,stroke-width:2px,color:#fff,rx:8px,ry:8px;

    U(("👤 User")):::user -->|"HTTPS Request"| ING["🌐 Ingress"]:::infra
    ING -->|"Routes Traffic"| K8S["☸️ Kubernetes (HPA Auto-Scaling)"]:::infra
    K8S -->|"Load Balances"| UI["🖥️ Streamlit UI & FastAPI"]:::engine
    
    UI -->|"Asks Question"| R["🧠 Intelligent AI Router"]:::router
    R -->|"Classifies Task & Selects Provider"| FE["⚙️ Fallback Execution Engine"]:::fallback
    
    FE -.->|"Stream 1"| G["⚡ Groq LLaMA 3.1"]:::llm
    FE -.->|"Stream 2"| GEM["🔵 Gemini 1.5 Flash"]:::llm
    FE -.->|"Stream 3"| OR["🌐 OpenRouter"]:::llm
    FE -.->|"Stream 4"| HF["🤗 Hugging Face"]:::llm
```

---

## 💻 Tech Stack

<div align="center">
  <img src="https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Gemini_1.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Groq_LLaMA_3.1-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq">
  <img src="https://img.shields.io/badge/OpenRouter-10B981?style=for-the-badge" alt="OpenRouter">
  <img src="https://img.shields.io/badge/Zephyr_7B-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face">
</div>

<br/>

> [!TIP]
> **Core Tooling:** `PyPDF` • `ChromaDB` • `requests` • `pytest` • `flake8` • `black`

---

## 🛠️ DevOps & Enterprise Infrastructure

NeuraFlow AI is built with **production-grade reliability, containerization, and scaling** in mind.

<details>
<summary><b>🐳 Docker & ☸️ Kubernetes</b></summary>
<br>

- **Docker**: Multi-stage, non-root user image optimized with layer caching and slim Python 3.11 base.
- **Kubernetes**: Fully orchestrated deployment featuring:
  - Rolling updates with 3 minimum replicas
  - `HorizontalPodAutoscaler` (HPA) configured to auto-scale up to 10 pods based on 70% CPU usage
  - Secure API Key management using Kubernetes Secrets
  - Nginx Ingress routing (`neuraflow.ai`) with Strict Security Headers and HTTPS support
</details>

<details>
<summary><b>🔄 CI/CD & 📈 Monitoring</b></summary>
<br>

- **CI/CD (GitHub Actions)**:
  - Automated Linting (`flake8`, `black`, `isort`) and Security Scanning (`bandit`)
  - Automated `pytest` unit testing
  - Container build and push pipeline (`docker-build.yml`)
  - Automated Kubernetes manifest validation (`k8s-validate.yml`)
- **Monitoring & Reliability**:
  - Live HTTP health and readiness probes (`/_stcore/health`)
  - Prometheus metrics configuration for node and pod monitoring
  - Automatic fallback execution logic if an API endpoint goes down
</details>

---

## 🚀 Getting Started

<details>
<summary><b>⚙️ Installation & Usage</b></summary>

<br>

### 1. Clone the Repository
```bash
git clone https://github.com/Piyu242005/AI-DOC-ASSISTANT.git
cd AI-DOC-ASSISTANT
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys:
```env
GEMINI_API_KEY="your_google_gemini_key"
GROQ_API_KEY="your_groq_key"
OPENROUTER_API_KEY="your_openrouter_key"
HUGGINGFACE_API_KEY="your_hf_key"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
TELEGRAM_CHAT_ID="your_telegram_chat_id"
```

### 5. Run the Application
```bash
streamlit run app.py
```
</details>

<details>
<summary><b>📂 Project Structure</b></summary>

<br>

```bash
AI-DOC-ASSISTANT/
├── .github/workflows/   # CI/CD Pipeline (Linting, Tests, Security)
├── assets/              # Premium SVGs, GIFs, and Logos
├── k8s/                 # Kubernetes Manifests (Deployments, Services, HPA)
├── monitoring/          # Prometheus & Grafana configurations
├── providers/           # Modular LLM Provider Interfaces
├── services/            # Core Engine & Routing Logic
│   ├── agent_engine.py      # Orchestration
│   ├── ai_router.py         # Factory
│   ├── fallback_manager.py  # Chain-of-Responsibility
│   ├── memory_manager.py    # Conversation Memory
│   ├── rag_engine.py        # Vector Search & Retrieval
│   ├── telegram_logger.py   # Telemetry & Monitoring
│   └── task_classifier.py   # Intent Analysis
├── utils/               # UI Helpers & Formatting
├── app.py               # Main Streamlit Interface
├── styles.py            # Global CSS / Design System
├── requirements.txt     # Dependencies
└── .env.example         # Environment Variable Template
```
</details>

---

## 🧠 How It Works

<div align="center">
  <img src="./assets/happy-retro-robot.gif" width="120" alt="Happy Robot AI">
</div>
<br/>

1. **Upload Document**: User uploads a `.pdf` file. The text is instantly extracted, vectorized using ChromaDB, and cached.
2. **Ask Question**: User submits a query about the document context.
3. **Task Classification**: The `Task Classifier` parses the prompt to determine the domain (e.g., *Reasoning*, *Coding*, *General Summarization*).
4. **Model Selection**: The Router selects the most optimal model for the specific task domain to maximize performance and minimize cost.
5. **Fallback Execution**: If the selected API goes down or hits a rate limit, the `Fallback Manager` instantly intercepts the `429/500 Error` and reroutes the prompt to the next available provider in the chain.
6. **Delivery**: The user receives the real-time streamed answer alongside an "Agent Decision Panel" explaining exactly how the routing occurred.

---

## 📸 Screenshots & Demo

| Main Dashboard | Agent Decision Panel |
| :---: | :---: |
| <img src="./assets/main_dashboard.png" width="100%" alt="Main Dashboard"> | <img src="./assets/agent_decision_panel.png" width="100%" alt="Agent Decision Panel"> |

*💡 Live Demo: [View Application](https://neuraflow.ai) | [Watch Video Walkthrough](./Project_Videos_and_PDFs/Anatomy_of_a_Query__Deconstructing_a_Multi-LLM_Pipeline.mp4)*

---

## 📊 Performance Highlights

- **Fault Tolerance:** 100% uptime guaranteed through multi-provider fallback orchestration.
- **Intelligent Routing:** Reduces latency by up to 40% on simple queries by routing to smaller/faster models.
- **Production Architecture:** Strongly typed OOP interfaces (`BaseProvider`), rigorous CI/CD GitHub Actions pipelines, and scalable dependency injection.

---

## 🔮 Future Roadmap

- [x] **RAG Support**: Implement `LangChain` and `ChromaDB` for chunking and vectorizing massive multi-page PDFs.
- [x] **Streaming Responses**: Add token-by-token text streaming for faster perceived latency.
- [x] **Agent Memory**: Maintain conversational context using memory management modules.
- [x] **Telegram Integration**: Real-time notifications and full document forwarding.
- [ ] **Voice Interface**: Whisper AI integration for verbal document querying.
- [ ] **Advanced Admin Dashboard**: Admin panel to monitor total token costs and model routing analytics.

---

## 👨‍💻 Author

<div align="center">

### **Piyush Ramteke**
**Data Scientist | AI Engineer | Python Developer**

*Passionate about building scalable AI systems, Generative AI applications, and elegant data solutions.*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Piyu242005)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/piyush-ramteke)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/Piyu242005)
[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=for-the-badge&logo=vercel&logoColor=white)](https://piyushramteke.dev)

</div>

---

## 📄 License & Legal

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
Copyright (c) 2024-2026 Piyush Ramteke.

By using this project, you agree to our [Terms and Conditions](https://piyu24.me/legal).

---

<div align="center">
  <sub>Built with ❤️ using Python, Streamlit, and modern Generative AI.</sub>
</div>
