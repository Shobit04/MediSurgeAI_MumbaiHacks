"""
Pharmaceutical AI Co-Pilot - Just-In-Time Medicine Production
Coordinates medicine supply chain for predicted surges
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class PharmaceuticalAgent:
    """
    Coordinates medicine supply chain and prevents stockouts
    """
    
    def __init__(self):
        self.partner_companies = [
            "Cipla", "Sun Pharma", "Dr. Reddy's", "Lupin", "Torrent Pharma"
        ]
        
        self.regional_hospitals = [
            "City Hospital", "Apollo Clinic", "Max Healthcare", 
            "Fortis Hospital", "Lilavati Hospital"
        ]
        
        logger.info("💊 Pharmaceutical AI Co-Pilot initialized")
    
    async def coordinate_supply(self, prediction: Dict) -> Dict:
        """Coordinate medicine supply for predicted surge"""
        
        predicted_patients = prediction.get("predicted_patients", 200)
        primary_condition = prediction.get("primary_condition", "")
        surge_date = prediction.get("surge_date", datetime.utcnow())
        
        # Determine medicine requirements
        medicine_requirements = self._calculate_medicine_needs(primary_condition, predicted_patients)
        
        # Check regional inventory
        regional_inventory = self._check_regional_inventory(medicine_requirements)
        
        # Alert pharmaceutical partners
        partner_alerts = self._alert_partners(medicine_requirements, surge_date)
        
        # Calculate supply status
        total_required = sum(m["quantity"] for m in medicine_requirements)
        total_available = sum(m["current_stock"] for m in regional_inventory)
        shortage = max(0, total_required - total_available)
        
        result = {
            "prediction_id": prediction.get("id"),
            "medicine_requirements": medicine_requirements,
            "regional_inventory": regional_inventory,
            "partner_alerts": partner_alerts,
            "total_required": total_required,
            "total_available": total_available,
            "shortage": shortage,
            "supply_status": "sufficient" if shortage == 0 else "shortage_detected",
            "estimated_delivery": surge_date - timedelta(hours=12),
            "timestamp": datetime.utcnow(),
            "status": "coordinating"
        }
        
        logger.info(
            f"💊 Pharmaceutical: Required {total_required} units, Available {total_available}, "
            f"Shortage {shortage}, Partners alerted: {len(partner_alerts)}"
        )
        
        return result
    
    def _calculate_medicine_needs(self, condition: str, patients: int) -> List[Dict]:
        """Calculate medicine requirements based on condition"""
        
        medicine_map = {
            "Respiratory Illness": [
                {"name": "Salbutamol Inhaler", "quantity_per_patient": 2, "unit": "doses"},
                {"name": "Corticosteroids", "quantity_per_patient": 1.5, "unit": "units"},
                {"name": "Antibiotics (Azithromycin)", "quantity_per_patient": 0.5, "unit": "courses"},
                {"name": "Oxygen Supply", "quantity_per_patient": 0.33, "unit": "cylinders"}
            ],
            "Viral Infections": [
                {"name": "Paracetamol", "quantity_per_patient": 3, "unit": "strips"},
                {"name": "Antivirals", "quantity_per_patient": 1, "unit": "courses"},
                {"name": "IV Fluids", "quantity_per_patient": 2, "unit": "bottles"}
            ],
            "Cardiovascular": [
                {"name": "Aspirin", "quantity_per_patient": 1, "unit": "strips"},
                {"name": "Beta Blockers", "quantity_per_patient": 1, "unit": "strips"},
                {"name": "ACE Inhibitors", "quantity_per_patient": 1, "unit": "strips"}
            ]
        }
        
        medicines = medicine_map.get(condition, medicine_map["Respiratory Illness"])
        
        requirements = []
        for med in medicines:
            requirements.append({
                "name": med["name"],
                "quantity": int(patients * med["quantity_per_patient"]),
                "unit": med["unit"],
                "critical": True
            })
        
        return requirements
    
    def _check_regional_inventory(self, requirements: List[Dict]) -> List[Dict]:
        """Check medicine availability across regional hospitals"""
        
        inventory = []
        for req in requirements:
            for hospital in self.regional_hospitals:
                current_stock = random.randint(0, req["quantity"])
                status = "sufficient" if current_stock >= req["quantity"] * 0.5 else "low"
                
                inventory.append({
                    "hospital": hospital,
                    "medicine": req["name"],
                    "current_stock": current_stock,
                    "required": req["quantity"] // len(self.regional_hospitals),
                    "unit": req["unit"],
                    "status": status,
                    "available_for_transfer": current_stock > req["quantity"] * 0.7
                })
        
        return inventory
    
    def _alert_partners(self, requirements: List[Dict], surge_date: datetime) -> List[Dict]:
        """Alert pharmaceutical partners for production ramp-up"""
        
        alerts = []
        for req in requirements:
            company = random.choice(self.partner_companies)
            production_capacity = int(req["quantity"] * random.uniform(1.2, 2.0))
            
            alert = {
                "partner_company": company,
                "medicine": req["name"],
                "requested_quantity": req["quantity"],
                "production_capacity": production_capacity,
                "production_status": random.choice(["ramping_up", "confirmed", "processing"]),
                "estimated_ready": surge_date - timedelta(hours=random.randint(12, 36)),
                "confidence": random.uniform(0.85, 0.98),
                "alerted_at": datetime.utcnow()
            }
            alerts.append(alert)
        
        return alerts
