'use client';

import { useEffect, useState } from 'react';
import { fetchAgentStatus } from '../lib/api';
import { CheckCircle, Activity, AlertCircle } from 'lucide-react';

export default function AgentStatus() {
  const [agents, setAgents] = useState<any>(null);

  useEffect(() => {
    loadAgents();
    const interval = setInterval(loadAgents, 15000);
    return () => clearInterval(interval);
  }, []);

  const loadAgents = async () => {
    try {
      const data = await fetchAgentStatus();
      setAgents(data.agents);
    } catch (error) {
      console.error('Error loading agents:', error);
    }
  };

  const agentList = [
    { key: 'orchestrator', name: 'Orchestrator', icon: '🎯', description: 'System Coordinator' },
    { key: 'surveillance', name: 'Surveillance', icon: '👁️', description: 'Data Monitor' },
    { key: 'prediction', name: 'Prediction', icon: '🔮', description: 'Surge Forecaster' },
    { key: 'resource', name: 'Resource', icon: '📦', description: 'Resource Planner' },
    { key: 'communication', name: 'Communication', icon: '📢', description: 'Public Advisory' },
    { key: 'insurance', name: 'Insurance', icon: '💰', description: 'Pre-Authorization' },
    { key: 'reverse911', name: 'Reverse 911', icon: '👨‍⚕️', description: 'Staff Activation' },
    { key: 'pharmaceutical', name: 'Pharmaceutical', icon: '💊', description: 'Supply Chain' },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      {agentList.map((agent) => (
        <div
          key={agent.key}
          className="card hover:shadow-lg transition-shadow cursor-pointer"
        >
          <div className="flex items-start justify-between mb-2">
            <span className="text-3xl">{agent.icon}</span>
            {agents?.[agent.key] && (
              <CheckCircle className="h-5 w-5 text-green-500" />
            )}
          </div>
          <h3 className="font-semibold text-gray-800 mb-1">{agent.name}</h3>
          <p className="text-xs text-gray-600 mb-2">{agent.description}</p>
          <div className="flex items-center space-x-1 text-xs">
            <Activity className="h-3 w-3 text-green-500 animate-pulse" />
            <span className="text-green-600 font-medium">Active</span>
          </div>
        </div>
      ))}
    </div>
  );
}
