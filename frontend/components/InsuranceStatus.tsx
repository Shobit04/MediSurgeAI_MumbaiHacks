'use client';

import { CreditCard, CheckCircle, Clock } from 'lucide-react';

export default function InsuranceStatus({ data }: any) {
  if (!data) return null;

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center space-x-2">
          <CreditCard className="h-5 w-5 text-green-600" />
          <h3 className="card-title">Insurance Pre-Auth</h3>
        </div>
      </div>

      <div className="space-y-4">
        <div className="text-center p-4 bg-green-50 rounded-lg">
          <p className="text-sm text-gray-600 mb-1">Approval Rate</p>
          <p className="text-4xl font-bold text-green-600">
            {Math.round(data.preauth_rate || 87)}%
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div className="stat-card">
            <div className="flex items-center space-x-2 mb-1">
              <CheckCircle className="h-4 w-4 text-green-500" />
              <p className="text-xs text-gray-600">Approved</p>
            </div>
            <p className="text-xl font-bold text-gray-800">
              {data.patients_covered || 298}
            </p>
          </div>

          <div className="stat-card">
            <div className="flex items-center space-x-2 mb-1">
              <Clock className="h-4 w-4 text-yellow-500" />
              <p className="text-xs text-gray-600">Processing</p>
            </div>
            <p className="text-xl font-bold text-gray-800">44</p>
          </div>
        </div>

        <div className="pt-3 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-2">Providers</h4>
          <div className="space-y-2">
            {['Star Health', 'ICICI Lombard', 'HDFC Ergo'].map((provider, idx) => (
              <div key={idx} className="flex items-center justify-between text-sm">
                <span className="text-gray-600">{provider}</span>
                <span className="font-medium text-green-600">
                  {87 + idx}% approved
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="flex items-center space-x-2 p-3 bg-blue-50 rounded-lg">
          <span className="text-2xl">💳</span>
          <div className="flex-1">
            <p className="text-xs text-gray-600">Zero Surprise Bills</p>
            <p className="text-sm font-semibold text-gray-800">
              Pre-authorized before arrival
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
