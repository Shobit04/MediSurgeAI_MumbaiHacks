"""
Agent status and control routes
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, AgentLog
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/status")
async def get_agents_status():
    """Get status of all agents"""
    return {
        "agents": {
            "orchestrator": {"status": "active", "uptime": "24/7"},
            "surveillance": {"status": "monitoring", "last_scan": datetime.utcnow().isoformat()},
            "prediction": {"status": "active", "accuracy": "87%"},
            "resource": {"status": "active", "calculations": "real-time"},
            "communication": {"status": "active", "channels": 4},
            "insurance": {"status": "active", "approval_rate": "87%"},
            "reverse911": {"status": "active", "staff_pool": 50},
            "pharmaceutical": {"status": "active", "partners": 5}
        },
        "system_health": "operational",
        "last_updated": datetime.utcnow().isoformat()
    }

@router.get("/logs")
async def get_agent_logs(limit: int = 50, db: Session = Depends(get_db)):
    """Get recent agent activity logs"""
    logs = db.query(AgentLog).order_by(AgentLog.timestamp.desc()).limit(limit).all()
    
    return {
        "logs": [
            {
                "id": log.id,
                "timestamp": log.timestamp.isoformat(),
                "agent": log.agent_name,
                "action": log.action,
                "status": log.status,
                "execution_time": log.execution_time
            }
            for log in logs
        ]
    }

@router.get("/activity")
async def get_agent_activity(hours: int = 24, db: Session = Depends(get_db)):
    """Get agent activity summary"""
    since = datetime.utcnow() - timedelta(hours=hours)
    logs = db.query(AgentLog).filter(AgentLog.timestamp >= since).all()
    
    # Group by agent
    activity = {}
    for log in logs:
        if log.agent_name not in activity:
            activity[log.agent_name] = {
                "total_actions": 0,
                "successful": 0,
                "failed": 0
            }
        activity[log.agent_name]["total_actions"] += 1
        if log.status == "success":
            activity[log.agent_name]["successful"] += 1
        else:
            activity[log.agent_name]["failed"] += 1
    
    return {
        "period_hours": hours,
        "activity": activity
    }
