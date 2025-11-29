"""
Orchestrator Agent - Coordinates all AI agents
"""

import asyncio
from datetime import datetime
from typing import Dict, List
import logging

from services.surveillance_agent import SurveillanceAgent
from services.prediction_agent import PredictionAgent
from services.resource_agent import ResourceAgent
from services.communication_agent import CommunicationAgent
from services.insurance_agent import InsuranceAgent
from services.reverse911_agent import Reverse911Agent
from services.pharmaceutical_agent import PharmaceuticalAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrchestratorAgent:
    """
    The Coordinator - Orchestrates all agents and prioritizes tasks
    """
    
    def __init__(self):
        logger.info("🎯 Initializing Orchestrator Agent...")
        
        # Initialize all agents
        self.surveillance = SurveillanceAgent()
        self.prediction = PredictionAgent()
        self.resource = ResourceAgent()
        self.communication = CommunicationAgent()
        self.insurance = InsuranceAgent()
        self.reverse911 = Reverse911Agent()
        self.pharmaceutical = PharmaceuticalAgent()
        
        self.monitoring_active = False
        logger.info("✅ Orchestrator Agent initialized!")
    
    async def start_monitoring(self):
        """Start 24/7 autonomous monitoring"""
        self.monitoring_active = True
        logger.info("🔄 Starting autonomous 24/7 monitoring...")
        
        while self.monitoring_active:
            try:
                # Step 1: Surveillance
                surveillance_data = await self.surveillance.monitor()
                logger.info(f"📊 Surveillance: Threat level {surveillance_data['threat_level']}")
                
                # Step 2: Prediction (if threat detected)
                if surveillance_data['threat_level'] in ['MEDIUM', 'HIGH', 'CRITICAL']:
                    prediction = await self.prediction.predict_surge(surveillance_data)
                    logger.info(f"🔮 Prediction: {prediction['confidence']}% confidence, {prediction['alert_level']} alert")
                    
                    # Step 3: Activate response agents if HIGH or CRITICAL
                    if prediction['alert_level'] in ['HIGH', 'CRITICAL']:
                        await self.coordinate_crisis_response(prediction)
                
                # Wait 15 minutes before next check
                await asyncio.sleep(900)
                
            except Exception as e:
                logger.error(f"❌ Error in monitoring loop: {e}")
                await asyncio.sleep(60)
    
    async def coordinate_crisis_response(self, prediction: Dict):
        """Coordinate all agents for crisis response"""
        logger.info(f"🚨 Coordinating crisis response for prediction ID: {prediction['id']}")
        
        try:
            # Execute all response agents in parallel
            results = await asyncio.gather(
                self.resource.allocate_resources(prediction),
                self.insurance.pre_authorize(prediction),
                self.reverse911.activate_staff(prediction),
                self.pharmaceutical.coordinate_supply(prediction),
                self.communication.send_advisory(prediction),
                return_exceptions=True
            )
            
            # Log results
            agent_names = ['Resource', 'Insurance', 'Reverse911', 'Pharmaceutical', 'Communication']
            for name, result in zip(agent_names, results):
                if isinstance(result, Exception):
                    logger.error(f"❌ {name} Agent failed: {result}")
                else:
                    logger.info(f"✅ {name} Agent: {result.get('status', 'completed')}")
            
            logger.info("🎉 Crisis response coordination complete!")
            
        except Exception as e:
            logger.error(f"❌ Error coordinating crisis response: {e}")
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.monitoring_active = False
        logger.info("🛑 Monitoring stopped")
    
    def get_system_status(self) -> Dict:
        """Get overall system status"""
        return {
            "orchestrator": "active" if self.monitoring_active else "idle",
            "agents": {
                "surveillance": "active",
                "prediction": "active",
                "resource": "active",
                "communication": "active",
                "insurance": "active",
                "reverse911": "active",
                "pharmaceutical": "active"
            },
            "monitoring": self.monitoring_active,
            "last_check": datetime.utcnow().isoformat()
        }
