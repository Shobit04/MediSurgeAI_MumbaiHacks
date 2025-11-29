'use client';

import { Package, Users, TrendingUp } from 'lucide-react';

export default function ResourceSummary({ data }: any) {
  if (!data) return null;

  const getStatusColor = (value: number) => {
    if (value >= 90) return 'text-green-600';
    if (value >= 70) return 'text-yellow-600';
    return 'text-red-600';
  };

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center space-x-2">
          <Package className="h-5 w-5 text-purple-600" />
          <h3 className="card-title">Resource Allocation</h3>
        </div>
        <span className="badge badge-success">Optimal</span>
      </div>

      <div className="space-y-4">
        {/* Staff Coverage */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center space-x-2">
              <Users className="h-4 w-4 text-gray-600" />
              <span className="text-sm font-medium text-gray-700">Staff Coverage</span>
            </div>
            <span className={`font-bold ${getStatusColor(data.staff_coverage || 92)}`}>
              {Math.round(data.staff_coverage || 92)}%
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-green-500 h-2 rounded-full transition-all"
              style={{ width: `${data.staff_coverage || 92}%` }}
            ></div>
          </div>
          <p className="text-xs text-gray-500 mt-1">
            12 additional nurses, 5 doctors allocated
          </p>
        </div>

        {/* Equipment Adequacy */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center space-x-2">
              <Package className="h-4 w-4 text-gray-600" />
              <span className="text-sm font-medium text-gray-700">Equipment Adequacy</span>
            </div>
            <span className={`font-bold ${getStatusColor(data.equipment_adequacy || 95)}`}>
              {Math.round(data.equipment_adequacy || 95)}%
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-green-500 h-2 rounded-full transition-all"
              style={{ width: `${data.equipment_adequacy || 95}%` }}
            ></div>
          </div>
          <p className="text-xs text-gray-500 mt-1">
            Oxygen, nebulizers, ventilators sufficient
          </p>
        </div>

        {/* Budget Utilization */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center space-x-2">
              <TrendingUp className="h-4 w-4 text-gray-600" />
              <span className="text-sm font-medium text-gray-700">Budget Utilization</span>
            </div>
            <span className={`font-bold ${getStatusColor(100 - (data.budget_utilization || 46))}`}>
              {Math.round(data.budget_utilization || 46)}%
            </span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-blue-500 h-2 rounded-full transition-all"
              style={{ width: `${data.budget_utilization || 46}%` }}
            ></div>
          </div>
          <p className="text-xs text-gray-500 mt-1">
            ₹2.28L allocated of ₹5L budget
          </p>
        </div>

        {/* Resource Breakdown */}
        <div className="pt-3 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-3">Equipment Details</h4>
          <div className="grid grid-cols-2 gap-3">
            <div className="bg-blue-50 p-3 rounded-lg">
              <p className="text-xs text-gray-600">Nebulizers</p>
              <p className="text-lg font-bold text-blue-600">48</p>
            </div>
            <div className="bg-blue-50 p-3 rounded-lg">
              <p className="text-xs text-gray-600">O₂ Cylinders</p>
              <p className="text-lg font-bold text-blue-600">114</p>
            </div>
            <div className="bg-blue-50 p-3 rounded-lg">
              <p className="text-xs text-gray-600">N95 Masks</p>
              <p className="text-lg font-bold text-blue-600">684</p>
            </div>
            <div className="bg-blue-50 p-3 rounded-lg">
              <p className="text-xs text-gray-600">Ventilators</p>
              <p className="text-lg font-bold text-blue-600">8</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
