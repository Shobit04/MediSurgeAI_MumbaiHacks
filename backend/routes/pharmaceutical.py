"""
Pharmaceutical and supply chain routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, PharmaceuticalInventory, PharmaceuticalAlert
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/inventory")
async def get_inventory_status(db: Session = Depends(get_db)):
    """Get pharmaceutical inventory status"""
    inventory = db.query(PharmaceuticalInventory).all()
    
    if not inventory:
        inventory = _generate_dummy_inventory()
    
    return {
        "hospitals": 5,
        "medicines_tracked": len(inventory),
        "inventory": [
            {
                "hospital": i.hospital_name if hasattr(i, 'hospital_name') else i.get('hospital_name'),
                "medicine": i.medicine_name if hasattr(i, 'medicine_name') else i.get('medicine_name'),
                "current_stock": i.current_stock if hasattr(i, 'current_stock') else i.get('current_stock'),
                "required_stock": i.required_stock if hasattr(i, 'required_stock') else i.get('required_stock'),
                "unit": i.unit if hasattr(i, 'unit') else i.get('unit'),
                "status": _get_stock_status(
                    i.current_stock if hasattr(i, 'current_stock') else i.get('current_stock'),
                    i.required_stock if hasattr(i, 'required_stock') else i.get('required_stock')
                )
            }
            for i in inventory
        ]
    }

@router.get("/alerts")
async def get_pharmaceutical_alerts(db: Session = Depends(get_db)):
    """Get pharmaceutical supply alerts"""
    alerts = db.query(PharmaceuticalAlert).order_by(
        PharmaceuticalAlert.timestamp.desc()
    ).limit(10).all()
    
    if not alerts:
        alerts = _generate_dummy_alerts()
    
    return {
        "active_alerts": len([a for a in alerts if _get_alert_status(a) == 'active']),
        "resolved_alerts": len([a for a in alerts if _get_alert_status(a) == 'resolved']),
        "alerts": [
            {
                "id": a.id if hasattr(a, 'id') else a.get('id'),
                "medicine": a.medicine_name if hasattr(a, 'medicine_name') else a.get('medicine_name'),
                "required": a.required_quantity if hasattr(a, 'required_quantity') else a.get('required_quantity'),
                "current_stock": a.current_stock if hasattr(a, 'current_stock') else a.get('current_stock'),
                "partner": a.partner_company if hasattr(a, 'partner_company') else a.get('partner_company'),
                "status": a.production_status if hasattr(a, 'production_status') else a.get('production_status'),
                "estimated_delivery": a.estimated_delivery.isoformat() if hasattr(a, 'estimated_delivery') and a.estimated_delivery else None
            }
            for a in alerts
        ]
    }

@router.get("/partners")
async def get_partner_companies():
    """Get pharmaceutical partner companies"""
    partners = [
        {
            "name": "Cipla",
            "active_orders": 12,
            "reliability_score": 94.5,
            "avg_delivery_time": "28 hours",
            "medicines_supplied": ["Salbutamol", "Corticosteroids", "Antibiotics"]
        },
        {
            "name": "Sun Pharma",
            "active_orders": 15,
            "reliability_score": 92.8,
            "avg_delivery_time": "32 hours",
            "medicines_supplied": ["Paracetamol", "Antivirals", "IV Fluids"]
        },
        {
            "name": "Dr. Reddy's",
            "active_orders": 8,
            "reliability_score": 96.2,
            "avg_delivery_time": "24 hours",
            "medicines_supplied": ["Aspirin", "Beta Blockers", "ACE Inhibitors"]
        },
        {
            "name": "Lupin",
            "active_orders": 10,
            "reliability_score": 91.5,
            "avg_delivery_time": "30 hours",
            "medicines_supplied": ["Antibiotics", "Antivirals", "Corticosteroids"]
        },
        {
            "name": "Torrent Pharma",
            "active_orders": 7,
            "reliability_score": 93.7,
            "avg_delivery_time": "26 hours",
            "medicines_supplied": ["Oxygen Supply", "IV Fluids", "Emergency Medicines"]
        }
    ]
    
    return {"partners": partners}

@router.get("/regional-buffer")
async def get_regional_buffer_pool():
    """Get regional medicine buffer pool status"""
    hospitals = ["City Hospital", "Apollo Clinic", "Max Healthcare", "Fortis Hospital", "Lilavati Hospital"]
    medicines = ["Salbutamol", "Corticosteroids", "Oxygen", "Antibiotics"]
    
    buffer_pool = []
    for hospital in hospitals:
        for medicine in medicines:
            excess = random.randint(0, 500)
            if excess > 200:
                buffer_pool.append({
                    "hospital": hospital,
                    "medicine": medicine,
                    "excess_stock": excess,
                    "available_for_transfer": True,
                    "expiry_date": (datetime.utcnow() + timedelta(days=random.randint(60, 180))).isoformat()
                })
    
    return {
        "total_transferable_items": len(buffer_pool),
        "buffer_pool": buffer_pool
    }

def _generate_dummy_inventory():
    """Generate dummy inventory data"""
    hospitals = ["City Hospital", "Apollo Clinic", "Max Healthcare", "Fortis Hospital"]
    medicines = [
        {"name": "Salbutamol Inhaler", "unit": "doses"},
        {"name": "Corticosteroids", "unit": "units"},
        {"name": "Oxygen Cylinders", "unit": "cylinders"},
        {"name": "Antibiotics", "unit": "courses"}
    ]
    
    inventory = []
    for hospital in hospitals:
        for med in medicines:
            inventory.append({
                "id": len(inventory) + 1,
                "hospital_name": hospital,
                "medicine_name": med["name"],
                "current_stock": random.randint(50, 500),
                "required_stock": random.randint(300, 600),
                "unit": med["unit"]
            })
    
    return inventory

def _generate_dummy_alerts():
    """Generate dummy pharmaceutical alerts"""
    medicines = ["Salbutamol Inhaler", "Corticosteroids", "Oxygen Cylinders", "Antibiotics"]
    partners = ["Cipla", "Sun Pharma", "Dr. Reddy's", "Lupin"]
    statuses = ["ramping_up", "confirmed", "ready"]
    
    alerts = []
    for i in range(5):
        alerts.append({
            "id": i + 1,
            "prediction_id": random.randint(1000, 9999),
            "medicine_name": random.choice(medicines),
            "required_quantity": random.randint(500, 2000),
            "current_stock": random.randint(100, 400),
            "partner_company": random.choice(partners),
            "production_status": random.choice(statuses),
            "estimated_delivery": datetime.utcnow() + timedelta(hours=random.randint(12, 48))
        })
    
    return alerts

def _get_stock_status(current, required):
    """Determine stock status"""
    ratio = current / required if required > 0 else 1
    if ratio >= 0.8:
        return "sufficient"
    elif ratio >= 0.5:
        return "low"
    else:
        return "critical"

def _get_alert_status(alert):
    """Determine alert status"""
    status = alert.production_status if hasattr(alert, 'production_status') else alert.get('production_status')
    return 'resolved' if status == 'ready' else 'active'
