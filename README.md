# AI Agent-based Deep Research System

## Overview
This project implements a dual-agent AI system for deep research using Tavily for web crawling and LangGraph for structuring responses.

## Features
- **Research Agent:** Fetches online information using Tavily API.
- **Answer Drafting Agent:** Uses GPT-4 to generate structured responses.
- **Vector Storage:** FAISS for persistent research data storage.
- **API Deployment:** FastAPI for query-based access.

## Installation
```bash
pip install -r requirements.txt
```

## Running the API
```bash
python main.py
```

## Example Usage
- Query: "Latest advancements in AI"
- Output: Structured AI-generated research summary

## File Structure
```
deep-research-agent/
│── main.py              # FastAPI for API deployment
│── agents.py            # Research & Answer Drafting Agents
│── vector_store.py      # FAISS-based vector database
│── requirements.txt     # Required dependencies
│── README.md            # Project documentation
│── docs/                # PDF documentation (to be added)
```

## Submission Details
- Submit **GitHub Repo + PDF Documentation + Resume** to `contact@kairon.co.in`
- **Deadline:** 7th March 2025
