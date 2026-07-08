# 🛡️ OpenRisk AI

> **AI-Powered Smart Contract Security Copilot**

OpenRisk AI is an AI-powered security analysis platform that helps blockchain developers identify potential vulnerabilities in Solidity smart contract repositories. By combining automated static analysis with Large Language Models (LLMs), OpenRisk AI transforms raw code metrics into actionable security insights and professional audit-style reports.

---

## 🚀 Overview

Smart contract audits are often expensive, time-consuming, and inaccessible to many development teams. OpenRisk AI bridges this gap by providing an automated first-pass security assessment for Solidity projects hosted on GitHub.

Users simply paste the URL of a public GitHub repository, and OpenRisk AI:

* Clones the repository
* Parses Solidity smart contracts
* Performs static security analysis
* Calculates an overall security risk score
* Generates an AI-powered executive security report

The goal is not to replace professional auditors but to help developers identify high-risk areas earlier in the development lifecycle.

---

## ✨ Features

* 🔍 GitHub repository analysis
* 📄 Automatic Solidity contract discovery
* 📊 Repository-wide security metrics
* ⚠️ Security risk scoring engine
* 🤖 AI-generated executive summaries
* ✅ Priority review recommendations
* 🚀 Actionable next steps for auditors and developers
* 🎨 Modern React dashboard

---

## 🏗️ Architecture

```text
                    GitHub Repository
                           │
                           ▼
                Repository Analyzer
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
 Static Contract Analysis              Repository Summary
        │                                     │
        └──────────────────┬──────────────────┘
                           ▼
                   Risk Scoring Engine
                           │
                           ▼
                 AI Report Generator (LLM)
                           │
                           ▼
                  FastAPI REST API
                           │
                           ▼
               React + TypeScript Frontend
```

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* GitPython
* Tree-sitter (Solidity parsing)
* Fireworks AI (LLM)
* Uvicorn

### Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* Axios

---

## 📂 Project Structure

```text
openrisk-ai/
│
├── backend/
│   ├── analysis/
│   ├── ai/
│   ├── ingestion/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── types/
│   │   └── App.tsx
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/openrisk-ai.git
cd openrisk-ai
```

---

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## 📡 API

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "healthy",
  "service": "OpenRisk AI",
  "version": "0.1.0"
}
```

---

### Analyze Repository

```http
POST /analyze
```

Request

```json
{
  "github_url": "https://github.com/Uniswap/v4-core"
}
```

Example Response

```json
{
  "analysis": {
    "repository": "...",
    "summary": {},
    "risk": {},
    "contracts": []
  },
  "ai_report": {
    "executive_summary": "...",
    "overall_security_posture": "Critical",
    "priority_review_areas": [],
    "recommended_next_steps": []
  }
}
```

---

## 📈 Example Workflow

1. Enter a public GitHub repository URL.
2. Click **Analyze**.
3. OpenRisk AI clones and analyzes the repository.
4. A repository-wide risk score is calculated.
5. An AI-generated audit report is displayed in the dashboard.

---

## 🎯 Future Improvements

* User authentication
* Saved analysis history
* PDF report export
* Repository comparison
* CI/CD integration
* Support for additional smart contract languages
* AI-powered vulnerability explanations
* Enterprise dashboard and team collaboration

---

## 🤝 Contributing

Contributions are welcome. If you'd like to improve OpenRisk AI, feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is released under the MIT License.

---

## 👤 Author

**Alice Mueti**

OpenRisk AI was developed to make smart contract security analysis faster, more accessible, and more actionable by combining automated analysis with AI-powered reporting.
