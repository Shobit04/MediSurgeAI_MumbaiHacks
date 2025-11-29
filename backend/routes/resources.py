"""
Resource allocation routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, Resource
import random

router = APIRouter()

@router.get("/current")
async def get_current_resources(db: Session = Depends(get_db)):
    """Get current resource allocations"""
    resources = db.query(Resource).order_by(Resource.timestamp.desc()).limit(5).all()
    
    if not resources:
        # Generate dummy resource allocation
        resources = [_generate_dummy_resources()]
    
    return {
        "allocations": [
            {
                "id": r.id if hasattr(r, 'id') else r.get('id'),
                "prediction_id": r.prediction_id if hasattr(r, 'prediction_id') else r.get('prediction_id'),
                "nurses_needed": r.nurses_needed if hasattr(r, 'nurses_needed') else r.get('nurses_needed'),
                "doctors_needed": r.doctors_needed if hasattr(r, 'doctors_needed') else r.get('doctors_needed'),
                "oxygen_cylinders": r.oxygen_cylinders if hasattr(r, 'oxygen_cylinders') else r.get('oxygen_cylinders'),
                "nebulizers": r.nebulizers if hasattr(r, 'nebulizers') else r.get('nebulizers'),
                "estimated_cost": r.estimated_cost if hasattr(r, 'estimated_cost') else r.get('estimated_cost')
            }
            for r in resources
        ]
    }

@router.get("/summary")
async def get_resource_summary():
    """Get resource allocation summary"""
    return {
        "staff": {
            "nurses_available": 45,
            "nurses_needed": 12,
            "doctors_available": 18,
            "doctors_needed": 5,
            "coverage": "adequate"
        },
        "equipment": {
            "nebulizers": {"available": 60, "needed": 48, "status": "sufficient"},
            "oxygen_cylinders": {"available": 200, "needed": 114, "status": "sufficient"},
            "ventilators": {"available": 25, "needed": 8, "status": "sufficient"},
            "n95_masks": {"available": 1000, "needed": 684, "status": "sufficient"}
        },
        "budget": {
            "allocated": 500000,
            "estimated_need": 228000,
            "remaining": 272000,
            "status": "within_budget"
        }
    }

def _generate_dummy_resources():
    """Generate dummy resource data"""
    return {
        "id": random.randint(100, 999),
        "prediction_id": random.randint(1000, 9999),
        "nurses_needed": random.randint(10, 15),
        "doctors_needed": random.randint(4, 7),
        "nebulizers": random.randint(40, 60),
        "oxygen_cylinders": random.randint(100, 130),
        "n95_masks": random.randint(600, 800),
        "ventilators": random.randint(5, 10),
        "estimated_cost": random.uniform(200000, 300000)
    }
