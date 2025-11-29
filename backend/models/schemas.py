"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

# Surveillance Models
class SurveillanceDataResponse(BaseModel):
    timestamp: datetime
    aqi: float
    temperature: float
    humidity: float
    events: Dict
    social_sentiment: Dict
    admission_patterns: Dict
    threat_level: str

    class Config:
        from_attributes = True

# Prediction Models
class PredictionResponse(BaseModel):
    id: int
    timestamp: datetime
    surge_date: datetime
    predicted_patients: int
    baseline_patients: int
    surge_percentage: float
    confidence: float
    primary_condition: str
    alert_level: str
    factors: Dict

    class Config:
        from_attributes = True

# Resource Models
class ResourceAllocation(BaseModel):
    nurses_needed: int
    doctors_needed: int
    nebulizers: int
    oxygen_cylinders: int
    n95_masks: int
    ventilators: int
    estimated_cost: float
    allocation_strategy: Dict

# Insurance Models
class InsurancePreAuthResponse(BaseModel):
    id: int
    prediction_id: int
    timestamp: datetime
    patient_count: int
    insurance_provider: str
    treatment_type: str
    estimated_cost: float
    status: str
    approval_rate: Optional[float]

    class Config:
        from_attributes = True

# Staff Models
class RetiredStaffProfile(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    distance_km: float
    crisis_hero_score: int
    availability: bool
    total_activations: int

    class Config:
        from_attributes = True

class StaffActivationRequest(BaseModel):
    staff_id: int
    shift_date: datetime
    shift_duration: int
    compensation: float

class StaffActivationResponse(BaseModel):
    id: int
    staff_id: int
    timestamp: datetime
    shift_date: datetime
    status: str
    response_time: Optional[float]

    class Config:
        from_attributes = True

# Pharmaceutical Models
class PharmaceuticalInventoryResponse(BaseModel):
    id: int
    hospital_name: str
    medicine_name: str
    current_stock: int
    required_stock: int
    unit: str
    stock_status: str

    class Config:
        from_attributes = True

class PharmaceuticalAlertResponse(BaseModel):
    id: int
    prediction_id: int
    medicine_name: str
    required_quantity: int
    current_stock: int
    partner_company: str
    production_status: str
    estimated_delivery: Optional[datetime]

    class Config:
        from_attributes = True

# Dashboard Models
class DashboardSummary(BaseModel):
    current_alert_level: str
    active_predictions: int
    total_patients_expected: int
    insurance_preauth_rate: float
    staff_activated: int
    medicine_stock_status: str
    last_updated: datetime

class AgentStatus(BaseModel):
    agent_name: str
    status: str
    last_action: str
    last_action_time: datetime
    success_rate: float
