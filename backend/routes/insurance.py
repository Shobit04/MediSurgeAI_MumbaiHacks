"""
Insurance pre-authorization routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, InsurancePreAuth
from datetime import datetime
import random

router = APIRouter()

@router.get("/status")
async def get_insurance_status(db: Session = Depends(get_db)):
    """Get insurance pre-authorization status"""
    recent = db.query(InsurancePreAuth).order_by(
        InsurancePreAuth.timestamp.desc()
    ).limit(10).all()
    
    if not recent:
        recent = [_generate_dummy_insurance() for _ in range(3)]
    
    # Calculate overall stats
    total_patients = sum(r.patient_count if hasattr(r, 'patient_count') else r.get('patient_count', 0) for r in recent)
    avg_approval = sum(r.approval_rate if hasattr(r, 'approval_rate') else r.get('approval_rate', 0) for r in recent) / len(recent) if recent else 0
    
    return {
        "total_preauth_requests": len(recent),
        "total_patients": total_patients,
        "average_approval_rate": round(avg_approval, 1),
        "recent_requests": [
            {
                "id": r.id if hasattr(r, 'id') else r.get('id'),
                "provider": r.insurance_provider if hasattr(r, 'insurance_provider') else r.get('insurance_provider'),
                "patient_count": r.patient_count if hasattr(r, 'patient_count') else r.get('patient_count'),
                "status": r.status if hasattr(r, 'status') else r.get('status'),
                "approval_rate": r.approval_rate if hasattr(r, 'approval_rate') else r.get('approval_rate')
            }
            for r in recent
        ]
    }

@router.get("/providers")
async def get_insurance_providers():
    """Get insurance provider statistics"""
    providers = [
        {"name": "Star Health", "preauth_count": 58, "approval_rate": 89.5, "avg_processing_time": "36 hours"},
        {"name": "ICICI Lombard", "preauth_count": 62, "approval_rate": 87.2, "avg_processing_time": "32 hours"},
        {"name": "HDFC Ergo", "preauth_count": 55, "approval_rate": 91.3, "avg_processing_time": "28 hours"},
        {"name": "Bajaj Allianz", "preauth_count": 48, "approval_rate": 85.8, "avg_processing_time": "40 hours"},
        {"name": "Max Bupa", "preauth_count": 42, "approval_rate": 88.7, "avg_processing_time": "34 hours"}
    ]
    
    return {"providers": providers}

@router.get("/treatments")
async def get_treatment_coverage():
    """Get treatment coverage information"""
    treatments = [
        {"name": "Emergency Consultation", "coverage_rate": 98.5, "avg_cost": 2000},
        {"name": "Nebulizer Therapy", "coverage_rate": 92.3, "avg_cost": 3500},
        {"name": "Oxygen Support", "coverage_rate": 94.7, "avg_cost": 5000},
        {"name": "Ventilator Use", "coverage_rate": 88.2, "avg_cost": 15000},
        {"name": "ICU Admission", "coverage_rate": 85.4, "avg_cost": 25000}
    ]
    
    return {"treatments": treatments}

def _generate_dummy_insurance():
    """Generate dummy insurance data"""
    providers = ["Star Health", "ICICI Lombard", "HDFC Ergo", "Bajaj Allianz", "Max Bupa"]
    return {
        "id": random.randint(100, 999),
        "prediction_id": random.randint(1000, 9999),
        "patient_count": random.randint(40, 80),
        "insurance_provider": random.choice(providers),
        "treatment_type": "Respiratory Care",
        "estimated_cost": random.uniform(150000, 300000),
        "status": random.choice(["approved", "approved", "pending"]),
        "approval_rate": random.uniform(82, 94),
        "timestamp": datetime.utcnow()
    }
