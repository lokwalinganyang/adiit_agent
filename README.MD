🚀 adiit_agent: Vector-Logistics Orchestrator
This repository contains the source code for the adiit_agent, a multi-tool Agent Development Kit (ADK) solution designed for the Build With AI (BWAI) Challenge. The agent serves as the Vector-Logistics Orchestrator for Turkana County, Kenya, synthesizing critical public health data (logistics, genomics, vectors) into a single, prioritized Daily Action Manifest for rapid emergency response.

🌟 Solution Overview
The adiit_agent solves the logistical and intelligence crisis caused by the convergence of drug-resistant Malaria and the Kala-azar (Leishmaniasis) epidemic.

It functions as a three-step Orchestration Pipeline:

Input Simulation: Two simulated Vertex AI tools provide high-dimensional data (Optimal Logistics Route, Multi-Disease Risk Indices).

LLM Synthesis (Genkit Core): The Gemini model processes these outputs using the generate_daily_action_manifest tool.

Actionable Output: It generates a single, clear memo containing non-negotiable, prioritized actions for the County CEO (e.g., redirecting the only logistics truck, mandating a drug protocol switch, initiating vector control).

🛠️ Setup Instructions
Follow these steps to set up and run the adiit_agent locally.

1. Prerequisites
Python 3.9+

A Gemini API Key (or a configured GCP project for Vertex AI).

ADK CLI installed: pip install google-adk

2. Clone and Structure
Create the required package structure and place the files (you should have four files in total: .env, __init__.py, agent.py, and the main PROJECT.md).

Bash

# Clone the repository (if applicable) or create the structure:
mkdir adiit_agent
cd adiit_agent
mkdir adiit_agent
# Place all generated files inside the inner 'adiit_agent' directory
3. Configure the Environment
Open the adiit_agent/.env file and set your API Key.

Code snippet

# adiit_agent/.env

# REQUIRED: Set your Gemini API Key
GEMINI_API_KEY="PASTE_YOUR_API_KEY_HERE"

# Optional: If running on Vertex AI, uncomment these lines:
# GOOGLE_GENAI_USE_VERTEXAI="True"
# GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
4. Install Dependencies
Navigate to the project root directory (the outer adiit_agent folder) and install the necessary Python packages.

Bash

# Ensure you are in the directory containing the inner 'adiit_agent' folder
python -m venv venv
source venv/bin/activate
pip install google-adk google-generativeai
🏃 Running the Agent
You can test the agent locally using the ADK Developer Web UI.

Start the ADK Server: From the project root directory, run:

Bash

adk web
Access the UI: Open your browser to the local URL (usually http://localhost:8080).

Execute the Critical Query: Select the adiit_agent from the list. Use the following prompt to demonstrate the multi-tool orchestration:

"Given all expiring stock, the nomadic camp movements, and the latest drug resistance reports, where should I send the single available logistics truck today to maximize life-saving impact and minimize wastage?"

Expected Output & Tool Trace
The agent will first call the two data-gathering tools (optimize_logistics_and_redistribution and generate_multi_disease_risk_report) and then use their structured outputs as input for the final orchestration tool (generate_daily_action_manifest) to produce the synthesized memo.