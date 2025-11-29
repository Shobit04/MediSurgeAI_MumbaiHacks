# MediSurge AI Frontend

Modern, responsive dashboard for the MediSurge AI Healthcare Crisis Management System.

## Setup Instructions

### 1. Install Dependencies
```bash
npm install
```

### 2. Run Development Server
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

### 3. Build for Production
```bash
npm run build
npm start
```

## Features

### Dashboard Components

1. **Header** - System status overview with key metrics
2. **Agent Status Grid** - Real-time status of all 8 AI agents
3. **Prediction Card** - Surge predictions with confidence levels
4. **Resource Summary** - Staff, equipment, and budget allocation
5. **Insurance Status** - Pre-authorization tracking and approval rates
6. **Staff Activation** - Retired medical staff mobilization
7. **Pharmaceutical Status** - Medicine supply chain coordination
8. **System Metrics** - Performance analytics and impact metrics
9. **Crisis Timeline** - Real-time event tracking

### Technology Stack

- **Framework**: Next.js 14 with App Router
- **UI Library**: React 18
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **Icons**: Lucide React
- **API Client**: Axios
- **TypeScript**: Full type safety

### Project Structure

```
frontend/
├── app/
│   ├── layout.tsx          # Root layout
│   └── page.tsx            # Main dashboard page
├── components/
│   ├── Header.tsx          # Header component
│   ├── AgentStatus.tsx     # Agent status grid
│   ├── PredictionCard.tsx  # Prediction display
│   ├── ResourceSummary.tsx # Resource allocation
│   ├── InsuranceStatus.tsx # Insurance tracking
│   ├── StaffActivation.tsx # Staff management
│   ├── PharmaceuticalStatus.tsx # Medicine supply
│   ├── SystemMetrics.tsx   # Performance metrics
│   └── CrisisTimeline.tsx  # Event timeline
├── lib/
│   └── api.ts              # API client functions
└── styles/
    └── globals.css         # Global styles
```

### API Integration

The frontend connects to the backend API at `http://localhost:8000/api`

All API calls are handled through the `lib/api.ts` module with automatic refresh intervals for real-time updates.

### Environment Variables

Create a `.env.local` file for custom configuration:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Features

- ⚡ **Real-time Updates** - Auto-refresh every 30 seconds
- 📊 **Interactive Charts** - Visualize system performance
- 🎨 **Modern UI** - Clean, professional design
- 📱 **Responsive** - Works on all device sizes
- 🔔 **Alert System** - Visual alerts for high-priority events
- 🎯 **Multi-Agent Tracking** - Monitor all 8 AI agents
- 📈 **Performance Metrics** - Comprehensive analytics dashboard

## Development

### Component Development
Each component is modular and can be developed independently. All components use TypeScript for type safety.

### Styling
Tailwind CSS utility classes are used throughout. Custom styles are defined in `globals.css`.

### Data Flow
1. Components fetch data from API via `lib/api.ts`
2. State management using React hooks
3. Automatic refresh intervals for real-time data
4. Loading states and error handling

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- Optimized bundle size
- Code splitting with Next.js
- Image optimization
- Lazy loading for charts
