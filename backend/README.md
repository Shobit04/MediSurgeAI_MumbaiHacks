# MediSurge AI Backend

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python main.py
```

The server will start on `http://localhost:8000`

### 3. API Documentation
Visit `http://localhost:8000/docs` for interactive API documentation

## API Endpoints

### Agents
- `GET /api/agents/status` - Get all agent statuses
- `GET /api/agents/logs` - Get agent activity logs
- `GET /api/agents/activity` - Get agent activity summary

### Predictions
- `GET /api/predictions/current` - Get active predictions
- `GET /api/predictions/history` - Get historical predictions
- `GET /api/predictions/{id}` - Get prediction details

### Resources
- `GET /api/resources/current` - Get current resource allocations
- `GET /api/resources/summary` - Get resource summary

### Insurance
- `GET /api/insurance/status` - Get insurance pre-auth status
- `GET /api/insurance/providers` - Get provider statistics
- `GET /api/insurance/treatments` - Get treatment coverage

### Staff (Reverse 911)
- `GET /api/staff/available` - Get available retired staff
- `GET /api/staff/activations` - Get staff activations
- `GET /api/staff/leaderboard` - Get Crisis Hero leaderboard

### Pharmaceutical
- `GET /api/pharmaceutical/inventory` - Get inventory status
- `GET /api/pharmaceutical/alerts` - Get supply alerts
- `GET /api/pharmaceutical/partners` - Get partner companies
- `GET /api/pharmaceutical/regional-buffer` - Get buffer pool

### Dashboard
- `GET /api/dashboard/summary` - Get comprehensive summary
- `GET /api/dashboard/metrics` - Get system metrics
- `GET /api/dashboard/timeline` - Get crisis timeline
- `GET /api/dashboard/agent-coordination` - Get coordination status

## WebSocket
- `ws://localhost:8000/ws/updates` - Real-time updates

## Database
SQLite database (`medisurge.db`) is automatically created on first run.

## Architecture

### Multi-Agent System
1. **Orchestrator Agent** - Coordinates all agents
2. **Surveillance Agent** - Monitors 20+ data sources
3. **Prediction Agent** - Predicts surges 48-72h ahead
4. **Resource Agent** - Calculates resource needs
5. **Communication Agent** - Sends public health advisories
6. **Insurance Agent** - Pre-authorizes insurance claims
7. **Reverse 911 Agent** - Activates retired medical staff
8. **Pharmaceutical Agent** - Coordinates medicine supply chain

All agents operate autonomously with dummy data for demonstration.
