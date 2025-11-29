"""
Surveillance Agent - The Watchful Eye
Monitors 20+ data sources 24/7
"""

import random
from datetime import datetime, timedelta
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class SurveillanceAgent:
    """
    Continuously monitors environmental and social data sources
    """
    
    def __init__(self):
        self.data_sources = [
            "weather_api", "aqi_monitor", "festival_calendar",
            "social_media", "hospital_admissions", "epidemic_tracker"
        ]
        logger.info("👁️  Surveillance Agent initialized")
    
    async def monitor(self) -> Dict:
        """Monitor all data sources and detect threats"""
        
        # Generate dummy surveillance data
        current_aqi = random.uniform(50, 300)
        temperature = random.uniform(15, 35)
        humidity = random.uniform(40, 85)
        
        # Check for upcoming festivals (dummy)
        upcoming_events = self._check_festivals()
        
        # Social media sentiment (dummy)
        social_sentiment = {
            "breathing_difficulty_mentions": random.randint(0, 1000),
            "hospital_queries": random.randint(0, 500),
            "sentiment_score": random.uniform(-1, 1)
        }
        
        # Hospital admission patterns
        admission_patterns = {
            "current_rate": random.randint(80, 150),
            "baseline": 100,
            "trend": random.choice(["increasing", "stable", "decreasing"])
        }
        
        # Determine threat level
        threat_level = self._calculate_threat_level(
            current_aqi, temperature, upcoming_events, 
            social_sentiment, admission_patterns
        )
        
        data = {
            "timestamp": datetime.utcnow(),
            "aqi": current_aqi,
            "temperature": temperature,
            "humidity": humidity,
            "events": upcoming_events,
            "social_sentiment": social_sentiment,
            "admission_patterns": admission_patterns,
            "threat_level": threat_level
        }
        
        logger.info(f"📊 Surveillance scan complete: AQI {current_aqi:.1f}, Temp {temperature:.1f}°C, Threat: {threat_level}")
        
        return data
    
    def _check_festivals(self) -> Dict:
        """Check for upcoming festivals/events"""
        festivals = ["Diwali", "Holi", "Dussehra", "New Year"]
        
        # Randomly determine if festival is upcoming
        days_until_festival = random.randint(0, 10)
        
        if days_until_festival <= 3:
            return {
                "upcoming": True,
                "name": random.choice(festivals),
                "days_until": days_until_festival
            }
        
        return {"upcoming": False, "name": None, "days_until": None}
    
    def _calculate_threat_level(self, aqi: float, temp: float, 
                                events: Dict, sentiment: Dict, 
                                admissions: Dict) -> str:
        """Calculate overall threat level"""
        
        score = 0
        
        # AQI factor
        if aqi > 200:
            score += 3
        elif aqi > 150:
            score += 2
        elif aqi > 100:
            score += 1
        
        # Temperature factor (cold weather)
        if temp < 20:
            score += 1
        
        # Events factor
        if events.get("upcoming") and events.get("days_until", 10) <= 2:
            score += 2
        
        # Social sentiment factor
        if sentiment.get("breathing_difficulty_mentions", 0) > 500:
            score += 2
        
        # Admission trend factor
        if admissions.get("trend") == "increasing":
            score += 1
        
        # Determine level
        if score >= 6:
            return "CRITICAL"
        elif score >= 4:
            return "HIGH"
        elif score >= 2:
            return "MEDIUM"
        else:
            return "LOW"
