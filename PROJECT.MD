# 🌍 V-LO Agent: Vector-Logistics Orchestrator (adiit_agent)

## 1. Problem Explanation (15 Points)

### What problem or workflow are you solving?
We are solving the systemic failure of **Public Health Logistics and Intelligence Orchestration** in resource-scarce regions like Turkana County, Kenya.

The traditional public health workflow is **manual, siloed, and reactive**:
1.  **Siloed Intelligence:** Operational data (drug expiry, vehicle status) is disconnected from critical scientific data (antimalarial **drug resistance** mutations, aggressive **vector shifts** like *Anopheles funestus* outdoor biting, and the concurrent **Kala-azar epidemic**).
2.  **Logistical Paralysis:** The County CEO, facing a critical **Logistics Failure** (e.g., only one vehicle operational), cannot efficiently answer the most crucial question: **"Where should I send the single available logistics truck today to maximize life-saving impact and minimize wastage across all disease programs?"**

### Why does it matter to a business or user?
This matters because failure to integrate intelligence leads directly to **preventable deaths and massive resource wastage**. The problem is a "Perfect Storm" of converging crises:
* **Financial Loss:** Millions of shillings worth of expensive Artemisinin Combination Therapy (AL) drugs expire due to poor redistribution planning.
* **Treatment Failure:** Emerging **Pfk13 C469Y** drug resistance mutations are ignored, leading to continued use of ineffective first-line treatment.
* **Epidemic Spread:** Logistical delays hamper the delivery of Amphotericin B to declared **Kala-azar (Visceral Leishmaniasis)** hotspots, raising the Case Fatality Rate (CFR).

---

## 2. Solution Showcase (AI Integration: 25 Points)

The **adiit\_agent** is a single, unified agent that transforms fragmented data into a single, **non-negotiable, Daily Action Manifest** for the County CEO.

### How the Solution Uses AI (Genkit, ADK, and Vertex AI)
The solution is a three-step **ADK/Genkit Orchestration Pipeline** that integrates specialized AI functions:

| Phase | Component | Technology | Rationale (What it Solves) |
| :--- | :--- | :--- | :--- |
| **A. Predictive Layer** | **Tool A & B (Vertex AI Simulation)** | Vertex AI / Python Function | Runs complex **Logistics Optimization** (minimizing wastage) and **Multi-Disease Risk Assessment** (predicting resistance and vector surge zones). |
| **B. Orchestration Layer** | **Tool C (`generate_daily_action_manifest`)** | **Genkit / LLM Reasoning** | The core reasoning step. The **Gemini LLM** synthesizes the high-dimensional, complex data outputs from the Vertex AI tools into a concise, human-readable plan. |
| **C. Delivery Layer** | **adiit\_agent (Root Agent)** | **Agent Development Kit (ADK)** | Defines the agent's role, instructions, and tool usage, ensuring the workflow is executed automatically upon a single user query. |

### Key Workflow: The Orchestration Loop
1.  **User Query:** CEO asks: *“Where should I send the truck today?”*
2.  **Agent Tool Call:** ADK calls **Tool A** (Logistics Optimization) and **Tool B** (Risk Report) in parallel.
3.  **Synthesis:** The LLM receives the outputs (e.g., *Optimal Route: Clinic 7* and *Risk Index: 0.88*).
4.  **Final Output:** The LLM generates the **Daily Action Manifest**, which includes logistics, a clinical protocol switch, and a vector control mandate, all in one prioritized document.

### Example Interaction (Key Question)
**User Input:** "Given all expiring stock, the nomadic camp movements, and the latest drug resistance reports, where should I send the single available logistics truck today to maximize life-saving impact and minimize wastage?"

**Agent Output (Tool C Synthesis):**
> **CRITICAL ACTION 1: Logistics & Wastage Mandate**
> * **Directive:** Immediately dispatch vehicle TCK-LGT-001 to Lodwar Central Depot to retrieve 950 units of Expiring AL 6s and deliver them to Mobile Clinic 7. Then, proceed to Clinic 10 to transfer excess Kala-azar drugs to Clinic 5.
> * **Rationale:** Prevents **$5,200 USD** in drug wastage while supporting the most vulnerable vector risk zone and Kala-azar emergency simultaneously.
>
> **CRITICAL ACTION 2: Drug Resistance Protocol Switch**
> * **Directive:** Mandate an immediate, official switch to second-line treatment at **CLINIC-A (Turkana South)**. Dispatch the Clinical Adherence team for non-punitive coaching on the **26.5% presumptive treatment rate**.
> * **Rationale:** The **Drug Resistance Risk Index is 0.88**, indicating high Pfk13 mutation frequency. Failure to switch guarantees treatment failure and parasite spread.
>
> **CRITICAL ACTION 3: Vector & Epidemic Alert**
> * **Directive:** Allocate two teams to the Clinic 5 catchment area for rapid **Kala-azar Case-Finding** and initiate **Larval Source Management (LSM)** in the urbanized zones near Clinic 7.
> * **Rationale:** Addresses the dual **sandfly (Kala-azar) and *Anopheles stephensi* (urban malaria)** vector threats identified by the predictive model.

---

## 3. Setup & Execution Instructions

1.  **Create Project Directory:**
    ```sh
    mkdir adiit_agent
    cd adiit_agent
    mkdir adiit_agent
    ```
2.  **Install Dependencies:**
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install google-adk google-generativeai
    ```
3.  **Create Files:**
    Create the files above (`adiit_agent/__init__.py`, `adiit_agent/agent.py`, `adiit_agent/.env`) and populate them with the provided code. **Crucially, fill in your API key in `.env`.**
4.  **Run the Agent:**
    ```sh
    # Navigate to the parent directory (one level above the 'adiit_agent' folder)
    cd ..
    # Start the ADK Web UI
    adk web
    ```
5.  Open your browser to the local URL (typically `http://localhost:8080`), select the **adiit\_agent**, and run the prompt.