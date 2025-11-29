"""
Database models and initialization for MediSurge AI
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database setup
DATABASE_URL = "sqlite:///./medisurge.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class SurveillanceData(Base):
    __tablename__ = "surveillance_data"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    aqi = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    events = Column(JSON)
    social_sentiment = Column(JSON)
    admission_patterns = Column(JSON)

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    surge_date = Column(DateTime)
    predicted_patients = Column(Integer)
    baseline_patients = Column(Integer)
    surge_percentage = Column(Float)
    confidence = Column(Float)
    primary_condition = Column(String)
    alert_level = Column(String)
    factors = Column(JSON)

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    nurses_needed = Column(Integer)
    doctors_needed = Column(Integer)
    nebulizers = Column(Integer)
    oxygen_cylinders = Column(Integer)
    n95_masks = Column(Integer)
    ventilators = Column(Integer)
    estimated_cost = Column(Float)
    allocation_strategy = Column(JSON)

class InsurancePreAuth(Base):
    __tablename__ = "insurance_preauth"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    patient_count = Column(Integer)
    insurance_provider = Column(String)
    treatment_type = Column(String)
    estimated_cost = Column(Float)
    status = Column(String)  # pending, approved, rejected
    approval_rate = Column(Float)

class RetiredStaff(Base):
    __tablename__ = "retired_staff"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)
    phone = Column(String)
    email = Column(String)
    distance_km = Column(Float)
    crisis_hero_score = Column(Integer, default=0)
    availability = Column(Boolean, default=True)
    last_response_time = Column(Float)  # hours
    total_activations = Column(Integer, default=0)

class StaffActivation(Base):
    __tablename__ = "staff_activations"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer)
    staff_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    shift_date = Column(DateTime)
    shift_duration = Column(Integer)  # hours
    compensation = Column(Float)
    status = Column(String)  # sent, confirmed, declined, completed
    response_time = Column(Float)  # hours

class PharmaceuticalInventory(Base):
    __tablename__ = "pharmaceutical_inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    hospital_name = Column(String)
    medicine_name = Column(String)
    current_stock = Column(Integer)
    required_stock = Column(Integer)
    unit = Column(String)
    expiry_date = Column(DateTime)
    last_updated = Column(DateTime, default=datetime.utcnow)

class PharmaceuticalAlert(Base):
    __tablename__ = "pharmaceutical_alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    medicine_name = Column(String)
    required_quantity = Column(Integer)
    current_stock = Column(Integer)
    partner_company = Column(String)
    production_status = Column(String)  # alerted, ramping, ready
    estimated_delivery = Column(DateTime)

class CommunicationLog(Base):
    __tablename__ = "communication_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    message_type = Column(String)  # advisory, activation, alert
    channel = Column(String)  # SMS, WhatsApp, email
    recipients_count = Column(Integer)
    content = Column(Text)
    language = Column(String)
    sent_successfully = Column(Boolean)

class AgentLog(Base):
    __tablename__ = "agent_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    agent_name = Column(String)
    action = Column(String)
    status = Column(String)
    details = Column(JSON)
    execution_time = Column(Float)

def init_db():
    """Initialize database and create tables"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
