"""
Resource Agent - The Strategic Planner
Calculates exact resource needs for predicted surges
"""

import random
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class ResourceAgent:
    """
    Calculates optimal resource allocation
    """
    
    def __init__(self):
        # Resource ratios per patient
        self.ratios = {
            "nurse_per_patient": 0.035,
            "doctor_per_patient": 0.015,
            "nebulizer_per_patient": 0.14,
            "oxygen_per_patient": 0.33,
            "mask_per_patient": 2.0,
            "ventilator_per_patient": 0.02,
            "cost_per_patient": 6667  # ₹ per patient
        }
        logger.info("📦 Resource Agent initialized")
    
    async def allocate_resources(self, prediction: Dict) -> Dict:
        """Calculate resource requirements for predicted surge"""
        
        predicted_patients = prediction.get("predicted_patients", 200)
        baseline_patients = prediction.get("baseline_patients", 120)
        additional_patients = predicted_patients - baseline_patients
        
        # Calculate staff needs
        nurses_needed = int(additional_patients * self.ratios["nurse_per_patient"]) + 1
        doctors_needed = int(additional_patients * self.ratios["doctor_per_patient"]) + 1
        
        # Calculate equipment needs
        nebulizers = int(additional_patients * self.ratios["nebulizer_per_patient"])
        oxygen_cylinders = int(additional_patients * self.ratios["oxygen_per_patient"])
        n95_masks = int(additional_patients * self.ratios["mask_per_patient"])
        ventilators = int(additional_patients * self.ratios["ventilator_per_patient"])
        
        # Calculate cost
        estimated_cost = additional_patients * self.ratios["cost_per_patient"]
        
        # Allocation strategy
        allocation_strategy = {
            "priority_1": "Staff allocation - critical",
            "priority_2": "Oxygen and respiratory equipment",
            "priority_3": "PPE and protective equipment",
            "deployment_timeline": "24 hours before surge",
            "contingency_buffer": "15% additional supplies"
        }
        
        resources = {
            "prediction_id": prediction.get("id"),
            "nurses_needed": nurses_needed,
            "doctors_needed": doctors_needed,
            "nebulizers": nebulizers,
            "oxygen_cylinders": oxygen_cylinders,
            "n95_masks": n95_masks,
            "ventilators": ventilators,
            "estimated_cost": estimated_cost,
            "allocation_strategy": allocation_strategy,
            "status": "calculated"
        }
        
        logger.info(
            f"📦 Resources: {nurses_needed} nurses, {doctors_needed} doctors, "
            f"{oxygen_cylinders} O2 cylinders, ₹{estimated_cost:,.0f}"
        )
        
        return resources
