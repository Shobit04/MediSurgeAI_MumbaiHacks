"""
Utility functions for data generation and processing
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict

def generate_time_series_data(days: int = 30) -> List[Dict]:
    """Generate time series data for charts"""
    data = []
    base_date = datetime.utcnow() - timedelta(days=days)
    
    for i in range(days):
        date = base_date + timedelta(days=i)
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "patients": random.randint(80, 180),
            "baseline": 120,
            "aqi": random.uniform(50, 250),
            "alerts": random.randint(0, 3)
        })
    
    return data

def calculate_surge_probability(aqi: float, temp: float, events: bool) -> float:
    """Calculate surge probability based on factors"""
    prob = 0.3  # Base probability
    
    if aqi > 200:
        prob += 0.4
    elif aqi > 150:
        prob += 0.2
    
    if temp < 20:
        prob += 0.2
    
    if events:
        prob += 0.3
    
    return min(prob, 0.95)

def format_currency(amount: float) -> str:
    """Format currency in Indian Rupees"""
    return f"₹{amount:,.0f}"

def calculate_percentage_change(current: float, baseline: float) -> float:
    """Calculate percentage change"""
    if baseline == 0:
        return 0
    return ((current - baseline) / baseline) * 100
