'use client';

import { TrendingUp, AlertTriangle, Calendar } from 'lucide-react';

export default function PredictionCard({ data }: any) {
  if (!data) return null;

  const getAlertColor = (level: string) => {
    switch (level) {
      case 'CRITICAL': return 'text-red-600 bg-red-50';
      case 'HIGH': return 'text-orange-600 bg-orange-50';
      case 'MEDIUM': return 'text-yellow-600 bg-yellow-50';
      default: return 'text-green-600 bg-green-50';
    }
  };

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center space-x-2">
          <TrendingUp className="h-5 w-5 text-blue-600" />
          <h3 className="card-title">Surge Prediction</h3>
        </div>
        <span className={`badge ${getAlertColor(data.primary_condition)}`}>
          {data.primary_condition || 'Respiratory'}
        </span>
      </div>

      <div className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div className="stat-card">
            <p className="text-sm text-gray-600 mb-1">Expected Patients</p>
            <p className="text-3xl font-bold text-blue-600">
              {data.total_patients_expected || 342}
            </p>
            <p className="text-xs text-gray-500 mt-1">
              Baseline: {data.baseline_patients || 120}
            </p>
          </div>

          <div className="stat-card">
            <p className="text-sm text-gray-600 mb-1">Surge Increase</p>
            <p className="text-3xl font-bold text-orange-600">
              +{Math.round(data.surge_percentage || 185)}%
            </p>
            <p className="text-xs text-gray-500 mt-1">
              vs. baseline
            </p>
          </div>
        </div>

        <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
          <div className="flex items-center space-x-2">
            <AlertTriangle className="h-5 w-5 text-blue-600" />
            <span className="text-sm font-medium text-gray-700">Confidence Level</span>
          </div>
          <span className="text-lg font-bold text-blue-600">
            {Math.round(data.confidence || 87)}%
          </span>
        </div>

        <div className="flex items-center space-x-2 text-sm text-gray-600">
          <Calendar className="h-4 w-4" />
          <span>Predicted 48-72 hours in advance</span>
        </div>

        <div className="pt-3 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-2">Contributing Factors</h4>
          <div className="flex flex-wrap gap-2">
            <span className="badge badge-info">AQI Spike</span>
            <span className="badge badge-info">Temperature Drop</span>
            <span className="badge badge-info">Festival Season</span>
            <span className="badge badge-info">Social Trends</span>
          </div>
        </div>
      </div>
    </div>
  );
}
