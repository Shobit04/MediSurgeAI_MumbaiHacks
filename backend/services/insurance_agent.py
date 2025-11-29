"""
Insurance Pre-Authorization Agent - Financial Crisis Prevention
Pre-processes insurance claims 48-72 hours before surge
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class InsuranceAgent:
    """
    Automates insurance pre-authorization for predicted patients
    """
    
    def __init__(self):
        self.insurance_providers = [
            "Star Health", "ICICI Lombard", "HDFC Ergo", 
            "Bajaj Allianz", "Max Bupa"
        ]
        self.treatment_costs = {
            "nebulizer_therapy": 3500,
            "oxygen_support": 5000,
            "ventilator_use": 15000,
            "icu_admission": 25000,
            "emergency_consultation": 2000
        }
        logger.info("💰 Insurance Pre-Authorization Agent initialized")
    
    async def pre_authorize(self, prediction: Dict) -> Dict:
        """Pre-authorize insurance for predicted patients"""
        
        predicted_patients = prediction.get("predicted_patients", 200)
        primary_condition = prediction.get("primary_condition", "")
        
        # Determine treatment types needed
        treatments = self._determine_treatments(primary_condition)
        
        # Calculate total cost
        total_cost = sum(self.treatment_costs[t] for t in treatments) * predicted_patients
        
        # Distribute patients across insurance providers
        authorizations = []
        patients_per_provider = predicted_patients // len(self.insurance_providers)
        
        for provider in self.insurance_providers:
            approval_rate = random.uniform(0.82, 0.92)
            approved_patients = int(patients_per_provider * approval_rate)
            
            auth = {
                "provider": provider,
                "patients": patients_per_provider,
                "approved": approved_patients,
                "pending": patients_per_provider - approved_patients,
                "treatments": treatments,
                "estimated_cost": (total_cost / len(self.insurance_providers)),
                "status": "processing"
            }
            authorizations.append(auth)
        
        # Overall approval rate
        total_approved = sum(a["approved"] for a in authorizations)
        overall_approval_rate = (total_approved / predicted_patients) * 100
        
        result = {
            "prediction_id": prediction.get("id"),
            "patient_count": predicted_patients,
            "treatments_covered": treatments,
            "total_estimated_cost": total_cost,
            "authorizations": authorizations,
            "total_approved": total_approved,
            "approval_rate": round(overall_approval_rate, 1),
            "processing_time": "24-48 hours",
            "timestamp": datetime.utcnow(),
            "status": "submitted"
        }
        
        logger.info(
            f"💰 Insurance: {total_approved}/{predicted_patients} patients pre-authorized "
            f"({overall_approval_rate:.1f}% approval rate), ₹{total_cost:,.0f}"
        )
        
        return result
    
    def _determine_treatments(self, condition: str) -> List[str]:
        """Determine required treatments based on condition"""
        
        treatment_map = {
            "Respiratory Illness": [
                "emergency_consultation", "nebulizer_therapy", 
                "oxygen_support", "ventilator_use"
            ],
            "Viral Infections": [
                "emergency_consultation", "oxygen_support"
            ],
            "Cardiovascular": [
                "emergency_consultation", "icu_admission", "oxygen_support"
            ]
        }
        
        return treatment_map.get(condition, ["emergency_consultation", "oxygen_support"])
