"""
Dashboard summary routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/summary")
async def get_dashboard_summary():
    """Get comprehensive dashboard summary"""
    return {
        "system_status": "operational",
        "monitoring_active": True,
        "last_updated": datetime.utcnow().isoformat(),
        
        "alerts": {
            "current_level": random.choice(["HIGH", "MEDIUM", "LOW"]),
            "active_predictions": random.randint(1, 3),
            "next_surge": (datetime.utcnow() + timedelta(hours=random.randint(48, 72))).isoformat()
        },
        
        "predictions": {
            "total_patients_expected": random.randint(300, 400),
            "baseline_patients": 120,
            "surge_percentage": random.uniform(150, 250),
            "confidence": random.uniform(85, 95),
            "primary_condition": random.choice(["Respiratory Illness", "Viral Infections"])
        },
        
        "resources": {
            "staff_coverage": random.uniform(85, 100),
            "equipment_adequacy": random.uniform(90, 100),
            "budget_utilization": random.uniform(40, 60)
        },
        
        "insurance": {
            "preauth_rate": random.uniform(85, 92),
            "patients_covered": random.randint(280, 350),
            "processing_status": "active"
        },
        
        "staff": {
            "activated_count": random.randint(10, 15),
            "available_pool": random.randint(35, 45),
            "response_rate": random.uniform(75, 90)
        },
        
        "pharmaceutical": {
            "supply_status": random.choice(["sufficient", "adequate", "low"]),
            "partners_engaged": 5,
            "medicines_secured": random.uniform(85, 98)
        },
        
        "communication": {
            "advisories_sent": random.randint(2, 5),
            "total_reach": random.randint(45000, 55000),
            "engagement_rate": random.uniform(65, 85)
        }
    }

@router.get("/metrics")
async def get_system_metrics():
    """Get detailed system metrics"""
    return {
        "performance": {
            "prediction_accuracy": 87.3,
            "average_response_time": "3.2 hours",
            "system_uptime": "99.8%",
            "agent_success_rate": 94.5
        },
        
        "capacity": {
            "max_patients_handleable": 500,
            "current_capacity_usage": random.uniform(40, 70),
            "staff_availability": random.uniform(75, 95),
            "equipment_utilization": random.uniform(50, 75)
        },
        
        "financial": {
            "total_budget": 500000,
            "allocated": random.uniform(200000, 300000),
            "insurance_covered": random.uniform(180000, 250000),
            "out_of_pocket_reduced": random.uniform(60, 80)
        },
        
        "impact": {
            "lives_protected": random.randint(800, 1200),
            "emergency_visits_prevented": random.randint(200, 400),
            "wait_time_reduction": random.uniform(50, 70),
            "stockouts_prevented": random.randint(5, 12)
        }
    }

@router.get("/timeline")
async def get_crisis_timeline():
    """Get crisis response timeline"""
    base_time = datetime.utcnow() - timedelta(hours=5)
    
    events = [
        {
            "time": base_time.isoformat(),
            "agent": "Surveillance",
            "event": "Threat detected: AQI spike + cold front + festival",
            "status": "completed"
        },
        {
            "time": (base_time + timedelta(minutes=5)).isoformat(),
            "agent": "Prediction",
            "event": "Surge predicted: 342 patients, 87% confidence",
            "status": "completed"
        },
        {
            "time": (base_time + timedelta(minutes=10)).isoformat(),
            "agent": "Resource",
            "event": "Resources calculated: 12 nurses, 5 doctors needed",
            "status": "completed"
        },
        {
            "time": (base_time + timedelta(minutes=13)).isoformat(),
            "agent": "Insurance",
            "event": "Pre-authorization submitted: 342 patients",
            "status": "processing"
        },
        {
            "time": (base_time + timedelta(minutes=15)).isoformat(),
            "agent": "Reverse 911",
            "event": "Staff activation: 15 notifications sent",
            "status": "in_progress"
        },
        {
            "time": (base_time + timedelta(minutes=18)).isoformat(),
            "agent": "Pharmaceutical",
            "event": "Partner alerts sent: 5 companies notified",
            "status": "completed"
        },
        {
            "time": (base_time + timedelta(minutes=20)).isoformat(),
            "agent": "Communication",
            "event": "Public advisory sent: 50,000+ recipients",
            "status": "completed"
        },
        {
            "time": (base_time + timedelta(hours=3)).isoformat(),
            "agent": "Reverse 911",
            "event": "Staff confirmations: 8 confirmed, 5 pending",
            "status": "in_progress"
        }
    ]
    
    return {
        "total_events": len(events),
        "timeline": events
    }

@router.get("/agent-coordination")
async def get_agent_coordination():
    """Get agent coordination status"""
    return {
        "orchestrator": {
            "status": "coordinating",
            "active_agents": 7,
            "tasks_queued": random.randint(2, 8),
            "tasks_completed": random.randint(15, 35)
        },
        
        "agent_interactions": [
            {"from": "Surveillance", "to": "Prediction", "type": "data_feed", "status": "active"},
            {"from": "Prediction", "to": "Resource", "type": "calculation_request", "status": "active"},
            {"from": "Prediction", "to": "Insurance", "type": "preauth_request", "status": "active"},
            {"from": "Prediction", "to": "Reverse911", "type": "activation_request", "status": "active"},
            {"from": "Prediction", "to": "Pharmaceutical", "type": "supply_request", "status": "active"},
            {"from": "Prediction", "to": "Communication", "type": "advisory_request", "status": "active"},
            {"from": "Resource", "to": "Reverse911", "type": "staff_requirements", "status": "completed"},
            {"from": "Resource", "to": "Pharmaceutical", "type": "equipment_needs", "status": "completed"}
        ],
        
        "coordination_efficiency": random.uniform(92, 98)
    }
