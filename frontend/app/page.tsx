'use client';

import { useEffect, useState } from 'react';
import Header from '../components/Header';
import AgentStatus from '../components/AgentStatus';
import PredictionCard from '../components/PredictionCard';
import ResourceSummary from '../components/ResourceSummary';
import InsuranceStatus from '../components/InsuranceStatus';
import StaffActivation from '../components/StaffActivation';
import PharmaceuticalStatus from '../components/PharmaceuticalStatus';
import SystemMetrics from '../components/SystemMetrics';
import CrisisTimeline from '../components/CrisisTimeline';
import { fetchDashboardData } from '../lib/api';

export default function Home() {
  const [dashboardData, setDashboardData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
    const interval = setInterval(loadDashboard, 30000); // Refresh every 30s
    return () => clearInterval(interval);
  }, []);

  const loadDashboard = async () => {
    try {
      const data = await fetchDashboardData();
      setDashboardData(data);
      setLoading(false);
    } catch (error) {
      console.error('Error loading dashboard:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading MediSurge AI...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Alert Banner */}
        {dashboardData?.alerts?.current_level !== 'LOW' && (
          <div className={`mb-6 p-4 rounded-lg ${
            dashboardData?.alerts?.current_level === 'CRITICAL' 
              ? 'bg-red-100 border-red-400 text-red-800' 
              : dashboardData?.alerts?.current_level === 'HIGH'
              ? 'bg-orange-100 border-orange-400 text-orange-800'
              : 'bg-yellow-100 border-yellow-400 text-yellow-800'
          } border-l-4`}>
            <div className="flex items-center">
              <span className="text-2xl mr-3">⚠️</span>
              <div>
                <p className="font-semibold">
                  {dashboardData?.alerts?.current_level} Alert Level
                </p>
                <p className="text-sm">
                  {dashboardData?.alerts?.active_predictions} active prediction(s) - 
                  Next surge expected in {Math.round(
                    (new Date(dashboardData?.alerts?.next_surge).getTime() - new Date().getTime()) / (1000 * 60 * 60)
                  )} hours
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Agent Status Grid */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">AI Agents Status</h2>
          <AgentStatus />
        </div>

        {/* Main Dashboard Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
          <PredictionCard data={dashboardData?.predictions} />
          <ResourceSummary data={dashboardData?.resources} />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
          <InsuranceStatus data={dashboardData?.insurance} />
          <StaffActivation data={dashboardData?.staff} />
          <PharmaceuticalStatus data={dashboardData?.pharmaceutical} />
        </div>

        {/* System Metrics */}
        <div className="mb-6">
          <SystemMetrics />
        </div>

        {/* Crisis Timeline */}
        <div className="mb-6">
          <CrisisTimeline />
        </div>

        {/* Footer */}
        <div className="text-center text-sm text-gray-500 mt-8 pt-6 border-t border-gray-200">
          <p>MediSurge AI v1.0.0 - Autonomous Healthcare Crisis Management System</p>
          <p className="mt-1">🤖 8 AI Agents Operating 24/7 | 🏥 Proactive Healthcare Resilience</p>
        </div>
      </main>
    </div>
  );
}
