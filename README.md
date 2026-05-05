# Medical Chatbot RAG Application
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/001c11c5-8ddc-418c-b53d-18ab7ac48363" />

 

# Project Architecture

```text
User Query
    ↓
Flask Backend
    ↓
LangChain RAG Pipeline
    ↓
Semantic Retrieval from Pinecone
    ↓
Relevant Context Extraction
    ↓
OpenAI LLM Response Generation
    ↓
Final AI Response
```

---

# Folder Structure

```text
medical_chatbot_rag_application/
│
├── src/
│   ├── __init__.py
│   ├── helper.py
│   ├── prompt.py
│   ├── retriever.py
│   ├── embeddings.py
│   └── utils.py
│
├── research/
│   └── trials.ipynb
│
├── data/
├── templates/
├── static/
│
├── app.py
├── requirements.txt
├── setup.py
├── Dockerfile
├── .env
├── README.md
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/medical_chatbot_rag_application.git
cd medical_chatbot_rag_application
```

---

## Create Conda Environment

```bash
conda create -n medical_chatbot python=3.10 -y
conda activate medical_chatbot
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file and add the following:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
```

---

# Run the Application

```bash
python app.py
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t medical-chatbot .
```

## Run Docker Container

```bash
docker run -p 5000:5000 medical-chatbot
```

---

# CI/CD Pipeline

Implemented CI/CD automation using GitHub Actions.

Pipeline includes:

* Automated build process
* Dependency installation
* Docker image creation
* Push Docker image to AWS ECR
* Automated deployment to AWS EC2

---

# AWS Deployment

## Services Used

* AWS EC2
* AWS ECR
* GitHub Actions

## Deployment Workflow

```text
GitHub Push
    ↓
GitHub Actions Trigger
    ↓
Docker Image Build
    ↓
Push to AWS ECR
    ↓
Deploy to AWS EC2
```

---

# Future Improvements

* Hybrid Search
* Conversation Memory
* Streaming Responses
* Authentication & Authorization
* Monitoring & Logging
* Kubernetes Deployment
* Evaluation Pipeline
* Multi-document Retrieval
* Medical Knowledge Base Expansion

---
# Author

Pprudhvivardhan
