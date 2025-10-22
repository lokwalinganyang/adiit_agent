# agent.py
# V-LO + ADIIT AI: Life-Saving Orchestrator for Turkana County Public Health
# Developer: Cleophas Ekuwom | Turkana West | October 22, 2025
# Challenge Fund: KES 300,000 – Digital Solutions for Climate Resilience

import os
import json
import datetime
from typing import Dict, Optional, Any
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.generativeai import GenerativeModel

# Load environment variables
load_dotenv()

# =============================================================================
# TURKANA 2025 HEALTH DATA (Triangulated from KHIS, MoH, Duke, Media)
# =============================================================================
TURKANA_DATA = {
    "emergency_declared": "2025-09-26",
    "kala_azar": {
        "cases_2025": 2043,
        "peak_june": 125,
        "deaths": 18,
        "cfr": 0.062,
        "demographics": {"male": 0.72, "under_24": 0.87, "malnourished": 0.20},
        "hotspots": ["Kerio", "Nakurio", "Nadoto", "Loima", "Kibish", "Kakuma"],
        "vectors": ["sandfly_anthills", "cracked_soil"]
    },
    "malaria": {
        "prevalence": 0.39,
        "smc_reduction_2024": 0.70,
        "kakuma_attack_rate_2005": 0.122,
        "habitats": ["tap_stand_pits", "drainage_channels"],
        "early_warning_model": {
            "threshold": 30,
            "tmax_code": [0,1,2,3,4,5],
            "rainfall_code": [0,1,2,3,4,5,6],
            "risk_formula": "Tmax_Code + Rainfall_Code"
        }
    },
    "gaps": {
        "blood": {"needed_quarter": 1000, "donated": 120},
        "stockouts": ["RK39", "DAT", "SSG_PM", "Amphotericin B"],
        "lost_followup": 25
    },
    "interventions": {
        "smc": True,
        "lsm": True,
        "four_pillar": True
    },
    "logistics": {
        "vehicles": 1,
        "facilities": 132,
        "area_km2": 71597
    }
}

# =============================================================================
# MALARIA RISK MODEL (MoH/KEMRI 2025) – Kakamega 45.5% Risk Aug 2025
# =============================================================================
def calculate_malaria_risk(tmax_anomaly: float, rainfall_mm: float) -> Dict[str, Any]:
    """
    MoH Early Warning Model: Tmax Anomaly + Rainfall → % Risk
    Threshold: 30% = Epidemic
    """
    tmax_code = min(int(tmax_anomaly // 0.5), 5)
    rainfall_code = min(int(rainfall_mm // 50), 6)
    risk_percent = (tmax_code + rainfall_code) * 10
    return {
        "risk_percent": risk_percent,
        "epidemic": risk_percent >= 30,
        "tmax_code": tmax_code,
        "rainfall_code": rainfall_code,
        "threshold": 30
    }

# =============================================================================
# TOOL 1: V-LO 3-STEP MANIFEST (Predictive Logistics)
# =============================================================================
def generate_vlo_manifest(query: str, tmax: Optional[float] = None, rain: Optional[float] = None) -> Dict[str, Any]:
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        risk_str = ""
        if tmax and rain:
            risk = calculate_malaria_risk(tmax, rain)
            risk_str = f"Malaria Risk: {risk['risk_percent']}% | Epidemic: {risk['epidemic']}"
        
        prompt = f"""
        You are V-LO Agent: Vector-Led Orchestration for Turkana Health.
        DATA: {json.dumps(TURKANA_DATA, indent=2)}
        QUERY: {query}
        {risk_str}
        
        Respond in 3 STEPS:
        1. LOGISTICS: Single truck route + supplies
        2. DETECTION: SMS/CHP alert to herders
        3. VECTOR: LSM, SMC, IRS action
        """
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "agent": "V-LO",
            "manifest": response.text.strip(),
            "generated_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat()
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =============================================================================
# TOOL 2: ADIIT CRISIS RESPONSE (4-Pillar Orchestration)
# =============================================================================
def generate_adiit_crisis_response(current_situation: str) -> Dict[str, Any]:
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        You are ADIIT Agent (Life-Saving Orchestrator). 'Adiit' = To Save in Turkana.
        DATA: {json.dumps(TURKANA_DATA, indent=2)}
        CRISIS: {current_situation}
        
        RESPOND IN 4 PRIORITIES:
        1. DRUG RESISTANCE & EXPIRY: Pfk13 mutations, Amphotericin B expiry
        2. LOGISTICS: Single truck routing across 132 facilities
        3. CLINICAL ADHERENCE: Support CHPs, simplify protocols
        4. VECTOR INTELLIGENCE: An. stephensi in Lodwar, sandfly hotspots
        
        OUTPUT: Actionable, time-bound, lives-saved estimate
        """
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "agent": "ADIIT",
            "crisis_response": response.text.strip(),
            "generated_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat()
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =============================================================================
# TOOL 3: EPIDEMIC INTELLIGENCE (30-Day Forecast)
# =============================================================================
def generate_epidemic_intelligence(surveillance_data: str) -> Dict[str, Any]:
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        Generate 30-DAY EPIDEMIC INTELLIGENCE for Turkana:
        DATA: {json.dumps(TURKANA_DATA, indent=2)}
        SURVEILLANCE: {surveillance_data}
        
        ANALYZE:
        - Vector dynamics (An. stephensi, An. funestus, sandflies)
        - Drug resistance (Pfk13 C469Y, P553L, A675V)
        - Nomadic mobility risks
        - Multi-disease hotspots
        
        PREDICT:
        - Risk zones next 30 days
        - Outbreak probability
        - Early warning signals
        - Mitigation strategy
        """
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "intelligence_report": response.text.strip(),
            "generated_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat()
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# =============================================================================
# ROOT AGENT – AUTO-DISCOVERED BY ADK
# =============================================================================
root_agent = Agent(
    name="turkana_health_agent",
    model="gemini-2.0-flash-exp",
    description="V-LO + ADIIT: AI for Turkana Public Health Emergency",
    instruction="""
    You are the unified AI agent for Turkana County Health Crisis.
    Your mission: Save lives using data, climate, logistics, and community.
    
    TOOLS:
    1. V-LO Manifest (3-step predictive response)
    2. ADIIT Crisis Response (4-pillar orchestration)
    3. Epidemic Intelligence (30-day forecast)
    
    Always respond with PRACTICAL, ACTIONABLE, LIFE-SAVING advice.
    """,
    tools=[
        generate_vlo_manifest,
        generate_adiit_crisis_response,
        generate_epidemic_intelligence
    ]
)

# =============================================================================
# TEST & INITIALIZATION
# =============================================================================
if __name__ == "__main__":
    print("V-LO + ADIIT AGENT INITIALIZED")
    print("Name: turkana_health_agent")
    print("Tools: 3 (V-LO, ADIIT, Intelligence)")
    print("Mission: Save 2,043 lives in Turkana")
    
    # Test V-LO
    test = generate_vlo_manifest("June 2025 surge in Loima?", tmax=2.0, rain=293.2)
    print("\nTEST V-LO MANIFEST:")
    print(test.get("manifest", test.get("message")))