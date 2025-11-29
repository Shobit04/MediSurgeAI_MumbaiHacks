# MediSurge AI - Quick Start Guide

## Prerequisites
- Python 3.11 or higher
- Node.js 18 or higher
- Git

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/Shobit04/MediSurgeAI_MumbaiHacks.git
cd MediSurgeAI_MumbaiHacks
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python main.py
```

Backend will start on `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/api/health`

### 3. Frontend Setup (New Terminal)
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

Frontend will start on `http://localhost:3000`

### 4. Access the Dashboard
Open your browser and navigate to:
```
http://localhost:3000
```

## Verification

### Backend Health Check
```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "agents": {
    "orchestrator": "active",
    "surveillance": "active",
    ...
  }
}
```

### Frontend
Visit `http://localhost:3000` and you should see:
- Header with system status
- 8 AI agent status cards
- Prediction cards
- Resource allocation
- Insurance status
- Staff activation
- Pharmaceutical status
- System metrics
- Crisis timeline

## Troubleshooting

### Backend Issues
1. **Port 8000 already in use**
   - Change port in `main.py`: `uvicorn.run(..., port=8001)`

2. **Module not found errors**
   - Ensure you're in the virtual environment
   - Run `pip install -r requirements.txt` again

3. **Database errors**
   - Delete `medisurge.db` and restart
   - Database will be recreated automatically

### Frontend Issues
1. **Port 3000 already in use**
   - Change port: `npm run dev -- -p 3001`

2. **Module not found errors**
   - Delete `node_modules` and `package-lock.json`
   - Run `npm install` again

3. **API connection errors**
   - Ensure backend is running on port 8000
   - Check `next.config.js` API proxy configuration

## Features to Explore

1. **Real-Time Monitoring**: Watch agents update every 15-30 seconds
2. **Agent Status Grid**: See all 8 agents operating
3. **Prediction System**: View predicted patient surges
4. **Resource Planning**: Check calculated resource needs
5. **Insurance Pre-Auth**: Track approval rates
6. **Staff Activation**: See Crisis Hero leaderboard
7. **Supply Chain**: Monitor pharmaceutical inventory
8. **Performance Metrics**: View system accuracy and uptime
9. **Crisis Timeline**: Follow event-by-event response

## Development Mode

### Backend with Auto-Reload
```bash
cd backend
python main.py
```
(Auto-reload is enabled by default in development)

### Frontend with Hot Reload
```bash
cd frontend
npm run dev
```
(Changes will reflect immediately)

## Production Build

### Backend
```bash
cd backend
# Install production dependencies
pip install -r requirements.txt

# Run with production settings
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend
```bash
cd frontend
# Build optimized production version
npm run build

# Start production server
npm start
```

## Environment Variables

### Backend
Create `.env` in backend folder (optional):
```env
DATABASE_URL=sqlite:///./medisurge.db
LOG_LEVEL=INFO
```

### Frontend
Create `.env.local` in frontend folder (optional):
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## System Requirements

### Minimum
- CPU: 2 cores
- RAM: 4 GB
- Storage: 1 GB

### Recommended
- CPU: 4+ cores
- RAM: 8+ GB
- Storage: 2+ GB
- Internet connection for package installation

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the main README.md for detailed documentation
3. Check API docs at `http://localhost:8000/docs`
4. Create an issue on GitHub

## Next Steps

1. ✅ Backend running on port 8000
2. ✅ Frontend running on port 3000
3. ✅ Dashboard accessible
4. 🚀 Explore the 8 AI agents in action
5. 📊 Monitor real-time crisis predictions
6. 🎯 Test different scenarios

**Welcome to MediSurge AI - Transforming Healthcare Crisis Management!** 🏥🤖
