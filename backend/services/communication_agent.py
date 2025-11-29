"""
Communication Agent - The Public Health Voice
Generates and distributes public health advisories
"""

import random
from datetime import datetime
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class CommunicationAgent:
    """
    Creates and distributes health advisories
    """
    
    def __init__(self):
        self.channels = ["SMS", "WhatsApp", "Email", "Social Media"]
        self.languages = ["English", "Hindi", "Marathi"]
        logger.info("📢 Communication Agent initialized")
    
    async def send_advisory(self, prediction: Dict) -> Dict:
        """Generate and send public health advisory"""
        
        condition = prediction.get("primary_condition", "Health Issue")
        surge_date = prediction.get("surge_date", datetime.utcnow())
        
        # Generate advisory message
        advisory = self._generate_advisory(condition, surge_date)
        
        # Simulate distribution
        recipients = random.randint(40000, 60000)
        
        # Multi-language distribution
        distributions = []
        for language in self.languages:
            for channel in self.channels:
                distributions.append({
                    "channel": channel,
                    "language": language,
                    "recipients": recipients // (len(self.languages) * len(self.channels)),
                    "sent": True
                })
        
        result = {
            "prediction_id": prediction.get("id"),
            "advisory_text": advisory,
            "total_recipients": recipients,
            "channels_used": self.channels,
            "languages": self.languages,
            "distributions": distributions,
            "timestamp": datetime.utcnow(),
            "status": "sent"
        }
        
        logger.info(f"📢 Advisory sent to {recipients:,} recipients via {len(self.channels)} channels")
        
        return result
    
    def _generate_advisory(self, condition: str, surge_date: datetime) -> str:
        """Generate health advisory text"""
        
        advisories = {
            "Respiratory Illness": (
                f"⚠️ HEALTH ADVISORY\n\n"
                f"Air quality concerns expected around {surge_date.strftime('%B %d')}. "
                f"Respiratory health precautions recommended:\n\n"
                f"✓ Wear N95 masks outdoors\n"
                f"✓ Limit outdoor activities\n"
                f"✓ Keep windows closed\n"
                f"✓ Use air purifiers if available\n"
                f"✓ Seek medical care if breathing difficulties arise\n\n"
                f"Stay safe! - City Health Department"
            ),
            "Viral Infections": (
                f"⚠️ HEALTH ADVISORY\n\n"
                f"Cold weather and viral activity expected around {surge_date.strftime('%B %d')}. "
                f"Prevention measures:\n\n"
                f"✓ Wash hands frequently\n"
                f"✓ Avoid crowded places\n"
                f"✓ Wear warm clothing\n"
                f"✓ Stay hydrated\n"
                f"✓ Seek medical care if fever persists\n\n"
                f"Stay healthy! - City Health Department"
            )
        }
        
        return advisories.get(condition, advisories["Respiratory Illness"])
