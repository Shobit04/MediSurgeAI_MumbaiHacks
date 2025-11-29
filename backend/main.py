"""
MediSurge AI - Main FastAPI Application
Multi-Agent Healthcare Crisis Management System
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from typing import List
import json

from routes import agents, predictions, resources, insurance, staff, pharmaceutical, dashboard
from services.orchestrator_agent import OrchestratorAgent
from database import init_db

# Initialize orchestrator
orchestrator = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for the application"""
    global orchestrator
    
    # Startup
    print("🚀 Initializing MediSurge AI System...")
    init_db()
    orchestrator = OrchestratorAgent()
    print("✅ All agents initialized and ready!")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down MediSurge AI System...")

# Initialize FastAPI app
app = FastAPI(
    title="MediSurge AI",
    description="Autonomous Multi-Agent Healthcare Crisis Management System",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(agents.router, prefix="/api/agents", tags=["Agents"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["Predictions"])
app.include_router(resources.router, prefix="/api/resources", tags=["Resources"])
app.include_router(insurance.router, prefix="/api/insurance", tags=["Insurance"])
app.include_router(staff.router, prefix="/api/staff", tags=["Staff"])
app.include_router(pharmaceutical.router, prefix="/api/pharmaceutical", tags=["Pharmaceutical"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "MediSurge AI - Healthcare Crisis Management System",
        "status": "operational",
        "version": "1.0.0"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "agents": {
            "orchestrator": "active",
            "surveillance": "active",
            "prediction": "active",
            "resource": "active",
            "communication": "active",
            "insurance": "active",
            "reverse911": "active",
            "pharmaceutical": "active"
        }
    }

@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time updates"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Echo back for now
            await manager.broadcast({
                "type": "update",
                "message": f"Received: {data}"
            })
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
