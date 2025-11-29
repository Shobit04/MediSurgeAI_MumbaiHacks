'use client';

import { useEffect, useState } from 'react';
import { fetchCrisisTimeline } from '../lib/api';
import { Clock, CheckCircle, AlertCircle, Loader } from 'lucide-react';

export default function CrisisTimeline() {
  const [timeline, setTimeline] = useState<any>(null);

  useEffect(() => {
    loadTimeline();
  }, []);

  const loadTimeline = async () => {
    try {
      const data = await fetchCrisisTimeline();
      setTimeline(data);
    } catch (error) {
      console.error('Error loading timeline:', error);
    }
  };

  if (!timeline) return null;

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="h-5 w-5 text-green-500" />;
      case 'in_progress':
        return <Loader className="h-5 w-5 text-blue-500 animate-spin" />;
      case 'processing':
        return <Clock className="h-5 w-5 text-yellow-500" />;
      default:
        return <AlertCircle className="h-5 w-5 text-gray-400" />;
    }
  };

  const getAgentColor = (agent: string) => {
    const colors: any = {
      'Surveillance': 'bg-blue-100 text-blue-800',
      'Prediction': 'bg-purple-100 text-purple-800',
      'Resource': 'bg-green-100 text-green-800',
      'Insurance': 'bg-yellow-100 text-yellow-800',
      'Reverse 911': 'bg-indigo-100 text-indigo-800',
      'Pharmaceutical': 'bg-pink-100 text-pink-800',
      'Communication': 'bg-orange-100 text-orange-800',
    };
    return colors[agent] || 'bg-gray-100 text-gray-800';
  };

  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-title">Crisis Response Timeline</h3>
        <span className="text-sm text-gray-600">
          {timeline.total_events} events recorded
        </span>
      </div>

      <div className="relative">
        {/* Timeline line */}
        <div className="absolute left-8 top-0 bottom-0 w-0.5 bg-gray-200"></div>

        {/* Timeline events */}
        <div className="space-y-4">
          {timeline.timeline?.map((event: any, idx: number) => (
            <div key={idx} className="relative flex items-start space-x-4 pl-4">
              {/* Icon */}
              <div className="relative z-10 flex-shrink-0">
                {getStatusIcon(event.status)}
              </div>

              {/* Content */}
              <div className="flex-1 bg-gray-50 rounded-lg p-4 hover:bg-gray-100 transition-colors">
                <div className="flex items-center justify-between mb-2">
                  <span className={`badge ${getAgentColor(event.agent)}`}>
                    {event.agent}
                  </span>
                  <span className="text-xs text-gray-500">
                    {new Date(event.time).toLocaleTimeString()}
                  </span>
                </div>
                <p className="text-sm text-gray-800">{event.event}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="mt-6 pt-4 border-t border-gray-200 flex items-center justify-between text-sm">
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <CheckCircle className="h-4 w-4 text-green-500" />
            <span className="text-gray-600">Completed</span>
          </div>
          <div className="flex items-center space-x-2">
            <Loader className="h-4 w-4 text-blue-500" />
            <span className="text-gray-600">In Progress</span>
          </div>
          <div className="flex items-center space-x-2">
            <Clock className="h-4 w-4 text-yellow-500" />
            <span className="text-gray-600">Processing</span>
          </div>
        </div>
        <span className="text-gray-500">Last updated: just now</span>
      </div>
    </div>
  );
}
