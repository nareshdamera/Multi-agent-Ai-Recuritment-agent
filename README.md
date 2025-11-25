

# 🤖 AI Recruiter Agency

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Gemini%201.5-orange?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**AI Recruiter Agency** is an intelligent, multi-agent recruitment system that automates the candidate evaluation process. Powered by **Google Gemini 1.5** and **Streamlit**, it orchestrates a team of specialized AI agents to extract, analyze, match, screen, and recommend candidates based on their PDF resumes.

---

## 📖 Table of Contents
- [Architecture](#-architecture)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Agent Workflow](#-agent-workflow)

---

## 🏗 Architecture

The system follows a **sequential multi-agent architecture** managed by a central Orchestrator.

<img width="2888" height="122" alt="Untitled diagram-2025-11-25-123822" src="https://github.com/user-attachments/assets/f8cba906-4e69-4903-8e1f-679594c3356b" />



✨ Key Features
📄 PDF Resume Parsing: Uses pdfminer.six to accurately extract text from PDF documents.

🔍 Deep Skill Analysis: The Analyzer Agent breaks down technical skills, experience level, and education.

🎯 Intelligent Job Matching: The Matcher Agent compares candidate profiles against a database of open positions to calculate compatibility scores.

🛡️ Automated Screening: The Screener Agent performs a qualitative "HR Screen" to identify red flags, cultural fit, and gaps.

💡 Strategic Recommendations: The Recommender Agent synthesizes all data to provide a final "Hire/No Hire" verdict with specific next steps.

📊 Interactive UI: A clean Streamlit interface to visualize every stage of the AI's reasoning process.



⚙ Configuration
To run the AI agents, you need a valid Google Gemini API Key.

Open agents/base_agent.py.

Locate the HARDCODED_API_KEY variable.

Replace the placeholder with your actual key:
