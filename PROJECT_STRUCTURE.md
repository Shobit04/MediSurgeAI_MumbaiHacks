# MediSurge AI - Project Structure

```
MediSurgeAI_MumbaiHacks/
│
├── backend/                        # FastAPI Backend
│   ├── main.py                    # Main FastAPI application
│   ├── database.py                # Database models and setup
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # Backend documentation
│   │
│   ├── models/                    # Data models
│   │   ├── __init__.py
│   │   └── schemas.py            # Pydantic schemas
│   │
│   ├── routes/                    # API routes
│   │   ├── __init__.py
│   │   ├── agents.py             # Agent status routes
│   │   ├── predictions.py        # Prediction routes
│   │   ├── resources.py          # Resource routes
│   │   ├── insurance.py          # Insurance routes
│   │   ├── staff.py              # Staff routes
│   │   ├── pharmaceutical.py     # Pharmaceutical routes
│   │   └── dashboard.py          # Dashboard routes
│   │
│   ├── services/                  # AI Agent Services
│   │   ├── __init__.py
│   │   ├── orchestrator_agent.py     # 🎯 Orchestrator
│   │   ├── surveillance_agent.py     # 👁️ Surveillance
│   │   ├── prediction_agent.py       # 🔮 Prediction
│   │   ├── resource_agent.py         # 📦 Resource
│   │   ├── communication_agent.py    # 📢 Communication
│   │   ├── insurance_agent.py        # 💰 Insurance
│   │   ├── reverse911_agent.py       # 👨‍⚕️ Reverse 911
│   │   └── pharmaceutical_agent.py   # 💊 Pharmaceutical
│   │
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── helpers.py
│
├── frontend/                       # Next.js Frontend
│   ├── package.json               # Node dependencies
│   ├── next.config.js             # Next.js configuration
│   ├── tailwind.config.js         # Tailwind CSS config
│   ├── tsconfig.json              # TypeScript config
│   ├── postcss.config.js          # PostCSS config
│   ├── README.md                  # Frontend documentation
│   │
│   ├── app/                       # Next.js App Router
│   │   ├── layout.tsx            # Root layout
│   │   └── page.tsx              # Main dashboard page
│   │
│   ├── components/                # React components
│   │   ├── Header.tsx            # Header component
│   │   ├── AgentStatus.tsx       # Agent status grid
│   │   ├── PredictionCard.tsx    # Prediction display
│   │   ├── ResourceSummary.tsx   # Resource allocation
│   │   ├── InsuranceStatus.tsx   # Insurance tracking
│   │   ├── StaffActivation.tsx   # Staff management
│   │   ├── PharmaceuticalStatus.tsx  # Medicine supply
│   │   ├── SystemMetrics.tsx     # Performance metrics
│   │   └── CrisisTimeline.tsx    # Event timeline
│   │
│   ├── lib/                       # Utilities
│   │   └── api.ts                # API client
│   │
│   └── styles/                    # Styling
│       └── globals.css           # Global styles
│
├── .gitignore                     # Git ignore file
├── README.md                      # Main documentation
├── SETUP.md                       # Setup instructions
└── setup.bat                      # Windows setup script
```

## Key Files

### Backend
- **main.py**: FastAPI application with CORS, WebSocket, and routes
- **database.py**: SQLAlchemy models for all data entities
- **services/**: 8 autonomous AI agents with dummy data
- **routes/**: REST API endpoints for each service

### Frontend
- **app/page.tsx**: Main dashboard with all components
- **components/**: Modular React components for each feature
- **lib/api.ts**: Axios-based API client with all endpoints
- **styles/globals.css**: Tailwind CSS custom styles

## Agent Architecture

1. **Orchestrator** → Coordinates all other agents
2. **Surveillance** → Monitors data sources
3. **Prediction** → Forecasts patient surges
4. **Resource** → Calculates resource needs
5. **Communication** → Sends public advisories
6. **Insurance** → Pre-authorizes insurance
7. **Reverse 911** → Activates retired staff
8. **Pharmaceutical** → Coordinates medicine supply

All agents use dummy data for demonstration purposes.
