"""
Retired staff and Reverse 911 routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, RetiredStaff, StaffActivation
from datetime import datetime
import random

router = APIRouter()

@router.get("/available")
async def get_available_staff(db: Session = Depends(get_db)):
    """Get available retired staff"""
    staff = db.query(RetiredStaff).filter(
        RetiredStaff.availability == True
    ).order_by(RetiredStaff.crisis_hero_score.desc()).limit(20).all()
    
    if not staff:
        staff = [_generate_dummy_staff() for _ in range(15)]
    
    return {
        "available_count": len(staff),
        "staff": [
            {
                "id": s.id if hasattr(s, 'id') else s.get('id'),
                "name": s.name if hasattr(s, 'name') else s.get('name'),
                "specialization": s.specialization if hasattr(s, 'specialization') else s.get('specialization'),
                "distance_km": s.distance_km if hasattr(s, 'distance_km') else s.get('distance_km'),
                "crisis_hero_score": s.crisis_hero_score if hasattr(s, 'crisis_hero_score') else s.get('crisis_hero_score'),
                "total_activations": s.total_activations if hasattr(s, 'total_activations') else s.get('total_activations')
            }
            for s in staff
        ]
    }

@router.get("/activations")
async def get_staff_activations(db: Session = Depends(get_db)):
    """Get recent staff activations"""
    activations = db.query(StaffActivation).order_by(
        StaffActivation.timestamp.desc()
    ).limit(20).all()
    
    if not activations:
        activations = [_generate_dummy_activation() for _ in range(8)]
    
    # Calculate stats
    confirmed = sum(1 for a in activations if (a.status if hasattr(a, 'status') else a.get('status')) == 'confirmed')
    pending = sum(1 for a in activations if (a.status if hasattr(a, 'status') else a.get('status')) == 'pending')
    
    return {
        "total_activations": len(activations),
        "confirmed": confirmed,
        "pending": pending,
        "response_rate": round((confirmed / len(activations) * 100), 1) if activations else 0,
        "activations": [
            {
                "id": a.id if hasattr(a, 'id') else a.get('id'),
                "staff_id": a.staff_id if hasattr(a, 'staff_id') else a.get('staff_id'),
                "shift_date": a.shift_date.isoformat() if hasattr(a, 'shift_date') and a.shift_date else None,
                "shift_duration": a.shift_duration if hasattr(a, 'shift_duration') else a.get('shift_duration'),
                "compensation": a.compensation if hasattr(a, 'compensation') else a.get('compensation'),
                "status": a.status if hasattr(a, 'status') else a.get('status')
            }
            for a in activations
        ]
    }

@router.get("/leaderboard")
async def get_crisis_hero_leaderboard(db: Session = Depends(get_db)):
    """Get Crisis Hero leaderboard"""
    staff = db.query(RetiredStaff).order_by(
        RetiredStaff.crisis_hero_score.desc()
    ).limit(10).all()
    
    if not staff:
        staff = [_generate_dummy_staff() for _ in range(10)]
        staff.sort(key=lambda x: x.get('crisis_hero_score', 0), reverse=True)
    
    return {
        "leaderboard": [
            {
                "rank": idx + 1,
                "name": s.name if hasattr(s, 'name') else s.get('name'),
                "specialization": s.specialization if hasattr(s, 'specialization') else s.get('specialization'),
                "crisis_hero_score": s.crisis_hero_score if hasattr(s, 'crisis_hero_score') else s.get('crisis_hero_score'),
                "total_activations": s.total_activations if hasattr(s, 'total_activations') else s.get('total_activations')
            }
            for idx, s in enumerate(staff)
        ]
    }

def _generate_dummy_staff():
    """Generate dummy staff data"""
    specializations = ["General Physician", "Respiratory Specialist", "Emergency Medicine", "ICU Specialist"]
    first_names = ["Dr. Rajesh", "Dr. Priya", "Dr. Amit", "Dr. Sneha", "Dr. Vikram"]
    last_names = ["Mehta", "Sharma", "Kumar", "Patel", "Singh"]
    
    return {
        "id": random.randint(1, 50),
        "name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "specialization": random.choice(specializations),
        "distance_km": round(random.uniform(2, 12), 1),
        "crisis_hero_score": random.randint(100, 500),
        "total_activations": random.randint(10, 45),
        "availability": True
    }

def _generate_dummy_activation():
    """Generate dummy activation data"""
    return {
        "id": random.randint(100, 999),
        "staff_id": random.randint(1, 50),
        "shift_date": datetime.utcnow(),
        "shift_duration": random.choice([4, 6, 8]),
        "compensation": random.choice([5333, 8000, 10667]),
        "status": random.choice(["confirmed", "confirmed", "pending", "declined"])
    }
