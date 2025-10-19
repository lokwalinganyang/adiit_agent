import os
import json
import datetime
from typing import Dict, Optional
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.generativeai import GenerativeModel

# Load environment variables
load_dotenv()

def generate_crisis_response_manifest(current_situation: str) -> dict:
    """
    Generate a crisis response manifest for Turkana County public health emergencies.
    """
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        You are Adiit Agent (Life-Saving Orchestrator) for Turkana County Public Health Emergency.
        
        CRITICAL SITUATION:
        {current_situation}
        
        Generate a PRIORITIZED CRISIS RESPONSE addressing:
        
        🚨 PRIORITY 1: DRUG RESISTANCE & EXPIRY EMERGENCY
        - Identify expiring commodities (AL packs, Amphotericin B)
        - Calculate redistribution to prevent wastage
        - Flag Pfk13 resistance mutations (C469Y, P553L, A675V)
        
        🚑 PRIORITY 2: MULTI-DISEASE LOGISTICS  
        - Balance malaria (An. stephensi, An. funestus) and Kala-azar responses
        - Optimize single vehicle routing across facilities
        - Coordinate last-mile distribution to nomadic communities
        
        🏥 PRIORITY 3: CLINICAL ADHERENCE
        - Address presumptive treatment rates
        - Generate supportive coaching for health workers
        - Simplify protocols for frontline staff
        
        🦟 PRIORITY 4: VECTOR INTELLIGENCE
        - Target An. stephensi urban breeding in Lodwar
        - Deploy control for insecticide-resistant An. funestus
        - Map Kala-azar sandfly hotspots
        
        Provide SPECIFIC, ACTIONABLE recommendations with:
        - Immediate actions
        - Resource allocation
        - Estimated impact
        """
        
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "crisis_manifest": response.text,
            "generated_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat(),
            "agent": "Adiit (Life-Saving Orchestrator)"
        }
        
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Failed to generate crisis manifest: {str(e)}"
        }

def optimize_vehicle_routing(stock_data: str) -> dict:
    """
    Optimize vehicle routing for drug distribution across Turkana County.
    """
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        Optimize SINGLE VEHICLE routing for Turkana County drug distribution:
        
        STOCK SITUATION:
        {stock_data}
        
        CONSTRAINTS:
        - Single available logistics vehicle
        - 71,597 km² harsh terrain
        - 132 health facilities
        - Limited fuel capacity
        
        Provide OPTIMAL ROUTING with:
        - Specific facility-to-facility movements
        - Quantities to redistribute
        - Estimated time for complete circuit
        - Lives saved projection
        """
        
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "routing_plan": response.text,
            "optimized_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat()
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Routing optimization failed: {str(e)}"
        }

def generate_epidemic_intelligence(surveillance_data: str) -> dict:
    """
    Generate epidemic intelligence and outbreak predictions.
    """
    try:
        model = GenerativeModel('gemini-2.0-flash-exp')
        prompt = f"""
        Generate EPIDEMIC INTELLIGENCE for Turkana County:
        
        SURVEILLANCE DATA:
        {surveillance_data}
        
        Analyze:
        - Vector dynamics (An. stephensi, An. funestus, sandflies)
        - Drug resistance patterns (Pfk13 mutations)
        - Mobility and transmission risks
        - Multi-disease hotspots
        
        Provide:
        - Risk assessment for next 30 days
        - Specific outbreak predictions
        - Early warning signals
        - Mitigation strategies
        """
        
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "intelligence_report": response.text,
            "generated_at": datetime.datetime.now(ZoneInfo("Africa/Nairobi")).isoformat()
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Intelligence generation failed: {str(e)}"
        }

# Create the agent - MUST be named 'root_agent' for ADK auto-discovery
root_agent = Agent(
    name="adiit_agent",
    model="gemini-2.0-flash-exp",
    description="Adiit Agent: Life-Saving Orchestrator for Turkana County Public Health Emergency",
    instruction="""
    You are Adiit Agent (Life-Saving Orchestrator) for Turkana County Public Health Emergency.
    Your name 'Adiit' means 'to save' in Turkana language.
    
    CRITICAL MISSIONS:
    1. Combat drug resistance (Pfk13 mutations) and prevent treatment failure
    2. Optimize logistics with single vehicle across 132 facilities
    3. Support health workers facing high clinical workloads
    4. Coordinate multi-disease response (Malaria + Kala-azar)
    5. Protect mobile pastoralist populations
    
    Always provide PRACTICAL, ACTIONABLE advice that saves lives and preserves dignity.
    """,
    tools=[
        generate_crisis_response_manifest,
        optimize_vehicle_routing, 
        generate_epidemic_intelligence,
    ],
)

print("✅ Adiit Agent initialized successfully!")
print("🤖 Name: adiit_agent")
print("🛠️ Tools: 3 (Crisis Response, Vehicle Routing, Epidemic Intelligence)")
print("🌍 Mission: Save lives in Turkana County")