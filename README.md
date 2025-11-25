🤖 AI Recruiter Agency








AI Recruiter Agency is an intelligent, multi-agent recruitment system that automates the candidate evaluation process.
Powered by Google Gemini 1.5 and Streamlit, it orchestrates a team of specialized AI agents to extract, analyze, match, screen, and recommend candidates based on their PDF resumes.

📖 Table of Contents

Architecture

Key Features

Installation

Configuration

Agent Workflow

🏗 Architecture

The system follows a sequential multi-agent architecture managed by a central Orchestrator.

<p align="center"> <img width="900" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/f8cba906-4e69-4903-8e1f-679594c3356b" /> </p>
✨ Key Features
📄 PDF Resume Parsing

Uses pdfminer.six for precise text extraction from candidate resumes.

🔍 Deep Skill Analysis

The Analyzer Agent evaluates:

Technical skills

Experience level

Education

Project depth & relevance

🎯 Intelligent Job Matching

The Matcher Agent compares:

Candidate profile

Available job database

Skill match score

Experience fit

🛡 Automated Screening

The Screener Agent conducts an AI-driven HR screening:

Identifies red flags

Checks gaps in experience

Evaluates communication clarity

Assesses cultural fit

💡 Strategic Recommendations

The Recommender Agent provides:

Hire/No-Hire decision

Strengths & weaknesses

Improvement suggestions

Recommended job roles

📊 Interactive UI

Built using Streamlit, showing:

Extracted resume text

Skill breakdown

Matching score

Final recommendation

⚙ Configuration

To run AI agents, you must configure your Google Gemini API Key.

Open:

agents/base_agent.py


Locate the variable:

HARDCODED_API_KEY = "YOUR_KEY_HERE"


Replace the placeholder with your actual Gemini API key.

🚀 Agent Workflow

The orchestration pipeline works as follows:

Extractor Agent

Reads the uploaded PDF

Converts it into raw structured text

Analyzer Agent

Breaks down skills, experience, education

Matcher Agent

Compares candidate profile with job descriptions

Generates compatibility scores

Screener Agent

Runs HR-style screening

Flags risks or inconsistencies

Recommender Agent

Produces the final output summary

Generates the "Hire / No Hire" recommendation
