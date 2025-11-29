"""
Reverse 911 Agent - Emergency Medical Staff Activation
Activates retired healthcare workers during predicted surges
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class Reverse911Agent:
    """
    Activates retired medical professionals for crisis support
    """
    
    def __init__(self):
        # Dummy retired staff database
        self.retired_staff_db = self._generate_staff_database()
        logger.info("👨‍⚕️ Reverse 911 Agent initialized with retired staff database")
    
    def _generate_staff_database(self) -> List[Dict]:
        """Generate dummy retired staff profiles"""
        
        specializations = [
            "General Physician", "Respiratory Specialist", "Emergency Medicine",
            "ICU Specialist", "Anesthesiologist", "General Surgeon"
        ]
        
        first_names = ["Dr. Rajesh", "Dr. Priya", "Dr. Amit", "Dr. Sneha", "Dr. Vikram", 
                      "Dr. Anjali", "Dr. Suresh", "Dr. Kavita", "Dr. Arun", "Dr. Meera"]
        last_names = ["Mehta", "Sharma", "Kumar", "Patel", "Singh", "Reddy", 
                     "Iyer", "Desai", "Gupta", "Nair"]
        
        staff = []
        for i in range(50):
            staff.append({
                "id": i + 1,
                "name": f"{random.choice(first_names)} {random.choice(last_names)}",
                "specialization": random.choice(specializations),
                "phone": f"+91-{random.randint(7000000000, 9999999999)}",
                "email": f"doctor{i+1}@retired.com",
                "distance_km": round(random.uniform(1, 15), 1),
                "crisis_hero_score": random.randint(50, 500),
                "availability": random.choice([True, True, True, False]),  # 75% available
                "last_response_time": round(random.uniform(0.5, 6), 1),  # hours
                "total_activations": random.randint(5, 50)
            })
        
        # Sort by crisis hero score (best responders first)
        staff.sort(key=lambda x: x["crisis_hero_score"], reverse=True)
        return staff
    
    async def activate_staff(self, prediction: Dict) -> Dict:
        """Activate retired staff for predicted surge"""
        
        predicted_patients = prediction.get("predicted_patients", 200)
        primary_condition = prediction.get("primary_condition", "")
        surge_date = prediction.get("surge_date", datetime.utcnow())
        
        # Calculate staff needed (from resource agent calculations)
        doctors_needed = max(5, int(predicted_patients * 0.015))
        nurses_needed = max(10, int(predicted_patients * 0.035))
        
        # Filter staff by specialization relevance
        relevant_specializations = self._get_relevant_specializations(primary_condition)
        relevant_staff = [
            s for s in self.retired_staff_db 
            if s["specialization"] in relevant_specializations and s["availability"]
        ]
        
        # Select top candidates
        candidates = relevant_staff[:doctors_needed * 2]  # Get 2x needed for redundancy
        
        # Send activation requests
        activations = []
        for staff in candidates[:doctors_needed + nurses_needed]:
            shift_duration = random.choice([4, 6, 8])
            compensation = shift_duration * 1333  # ₹8,000 for 6 hours
            
            activation = {
                "staff_id": staff["id"],
                "staff_name": staff["name"],
                "specialization": staff["specialization"],
                "phone": staff["phone"],
                "distance_km": staff["distance_km"],
                "shift_date": surge_date,
                "shift_duration": shift_duration,
                "compensation": compensation,
                "status": random.choice(["confirmed", "confirmed", "pending", "declined"]),
                "response_time": round(random.uniform(0.5, 3), 1),
                "sent_at": datetime.utcnow()
            }
            activations.append(activation)
        
        # Calculate statistics
        confirmed = len([a for a in activations if a["status"] == "confirmed"])
        pending = len([a for a in activations if a["status"] == "pending"])
        declined = len([a for a in activations if a["status"] == "declined"])
        
        result = {
            "prediction_id": prediction.get("id"),
            "doctors_needed": doctors_needed,
            "nurses_needed": nurses_needed,
            "activations_sent": len(activations),
            "confirmed": confirmed,
            "pending": pending,
            "declined": declined,
            "coverage_rate": round((confirmed / (doctors_needed + nurses_needed)) * 100, 1),
            "activations": activations,
            "timestamp": datetime.utcnow(),
            "status": "active"
        }
        
        logger.info(
            f"👨‍⚕️ Reverse 911: {confirmed}/{len(activations)} confirmed, "
            f"{pending} pending, {coverage_rate}% coverage"
        )
        
        return result
    
    def _get_relevant_specializations(self, condition: str) -> List[str]:
        """Get relevant medical specializations for condition"""
        
        specialization_map = {
            "Respiratory Illness": [
                "Respiratory Specialist", "Emergency Medicine", 
                "ICU Specialist", "General Physician"
            ],
            "Viral Infections": [
                "General Physician", "Emergency Medicine", "ICU Specialist"
            ],
            "Cardiovascular": [
                "ICU Specialist", "Emergency Medicine", 
                "Anesthesiologist", "General Physician"
            ]
        }
        
        return specialization_map.get(condition, ["General Physician", "Emergency Medicine"])
