# 🤖 AI Recruiter Agency

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Gemini%201.5-orange?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**AI Recruiter Agency** is an intelligent, multi-agent recruitment system built using **Google Gemini 1.5** and **Streamlit**.  
It automates the candidate evaluation process through a pipeline of specialized AI agents that extract, analyze, match, screen, and recommend candidates using their PDF resumes.

---

## 📖 Table of Contents
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Agent Workflow](#agent-workflow)

---

## 🏗 Architecture

The system follows a **sequential multi-agent architecture**, all managed by a central **Orchestrator**.

<p align="center">
  <img width="900" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/f8cba906-4e69-4903-8e1f-679594c3356b" />
</p>

---

## ✨ Key Features

### 📄 PDF Resume Parsing  
Uses **pdfminer.six** to extract clean text from PDF resumes with high accuracy.

### 🔍 Deep Skill Analysis  
The **Analyzer Agent** evaluates:
- Technical skills  
- Experience level  
- Education  
- Project relevance  
- Domain expertise  

### 🎯 Intelligent Job Matching  
The **Matcher Agent** compares candidate strengths with job descriptions to generate:
- Skill match percentage  
- Experience alignment  
- Domain compatibility  

### 🛡 Automated HR Screening  
The **Screener Agent** performs qualitative analysis:
- Detects red flags  
- Identifies missing skills  
- Evaluates cultural fit  
- Checks communication clarity  

### 💡 Final Recommendation  
The **Recommender Agent** provides a decision:
- ✔ Hire  
- ❌ No Hire  
- Suggestions for improvement  
- Recommended job roles  

### 📊 Interactive UI  
A modern **Streamlit Web Interface** to visualize:
- Resume text  
- Skill breakdown  
- Job matching score  
- Screening summary  
- Final verdict  

---

## ⚙ Configuration

To run the AI agents, configure your **Gemini API Key**.

1. Open:

```bash
agents/base_agent.py
Find the variable:

HARDCODED_API_KEY = "YOUR_KEY_HERE"


Replace "YOUR_KEY_HERE" with your actual Gemini API key.

🚀 Agent Workflow
1. Extractor Agent

Reads and extracts raw text from the uploaded PDF.

2. Analyzer Agent

Identifies skills, education, experience, and strengths.

3. Matcher Agent

Compares candidate profile with open job roles.

Generates match scores.

4. Screener Agent

Performs soft-skill & HR-level evaluation.

Flags concerns or inconsistencies.

5. Recommender Agent

Summarizes all results.

Provides the final Hire / No Hire decision.

📌 Tech Stack
Component	Technology
Language	Python 3.10+
Framework	Streamlit
AI Model	Google Gemini 1.5
PDF Parsing	pdfminer.six
Architecture	Multi-Agent Orchestration
