'use client';

import { Pill, TrendingUp, AlertCircle } from 'lucide-react';

export default function PharmaceuticalStatus({ data }: any) {
  if (!data) return null;

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'sufficient': return 'text-green-600 bg-green-50';
      case 'adequate': return 'text-blue-600 bg-blue-50';
      case 'low': return 'text-yellow-600 bg-yellow-50';
      default: return 'text-red-600 bg-red-50';
    }
  };

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center space-x-2">
          <Pill className="h-5 w-5 text-pink-600" />
          <h3 className="card-title">Pharmaceutical</h3>
        </div>
      </div>

      <div className="space-y-4">
        <div className={`text-center p-4 rounded-lg ${getStatusColor(data.supply_status || 'sufficient')}`}>
          <p className="text-sm mb-1">Supply Status</p>
          <p className="text-2xl font-bold capitalize">
            {data.supply_status || 'Sufficient'}
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div className="stat-card">
            <p className="text-xs text-gray-600 mb-1">Partners Engaged</p>
            <p className="text-2xl font-bold text-gray-800">
              {data.partners_engaged || 5}
            </p>
          </div>

          <div className="stat-card">
            <p className="text-xs text-gray-600 mb-1">Medicines Secured</p>
            <p className="text-2xl font-bold text-green-600">
              {Math.round(data.medicines_secured || 92)}%
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2 p-3 bg-blue-50 rounded-lg">
          <TrendingUp className="h-5 w-5 text-blue-600" />
          <div className="flex-1">
            <p className="text-xs text-gray-600">Production Status</p>
            <p className="text-sm font-semibold text-gray-800">
              Ramping up for surge
            </p>
          </div>
        </div>

        <div className="pt-3 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-2">Critical Medicines</h4>
          <div className="space-y-2">
            {[
              { name: 'Salbutamol', status: 'sufficient', stock: 2500 },
              { name: 'Corticosteroids', status: 'sufficient', stock: 1800 },
              { name: 'Oxygen Supply', status: 'adequate', stock: 850 },
            ].map((med, idx) => (
              <div key={idx} className="flex items-center justify-between text-sm">
                <span className="text-gray-700">{med.name}</span>
                <div className="flex items-center space-x-2">
                  <span className="text-xs text-gray-500">{med.stock} units</span>
                  <span className={`badge ${med.status === 'sufficient' ? 'badge-success' : 'badge-info'}`}>
                    {med.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="flex items-center space-x-2 text-xs text-gray-600 p-2 bg-gray-50 rounded">
          <AlertCircle className="h-4 w-4" />
          <span>72-hour advance alerts sent to partners</span>
        </div>
      </div>
    </div>
  );
}
