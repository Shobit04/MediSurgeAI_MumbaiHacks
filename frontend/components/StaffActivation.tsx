'use client';

import { Users, Award, Phone } from 'lucide-react';

export default function StaffActivation({ data }: any) {
  if (!data) return null;

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center space-x-2">
          <Users className="h-5 w-5 text-indigo-600" />
          <h3 className="card-title">Staff Activation</h3>
        </div>
      </div>

      <div className="space-y-4">
        <div className="text-center p-4 bg-indigo-50 rounded-lg">
          <p className="text-sm text-gray-600 mb-1">Activated</p>
          <p className="text-4xl font-bold text-indigo-600">
            {data.activated_count || 12}
          </p>
          <p className="text-xs text-gray-500 mt-1">retired professionals</p>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div className="stat-card">
            <p className="text-xs text-gray-600 mb-1">Available Pool</p>
            <p className="text-2xl font-bold text-gray-800">
              {data.available_pool || 38}
            </p>
          </div>

          <div className="stat-card">
            <p className="text-xs text-gray-600 mb-1">Response Rate</p>
            <p className="text-2xl font-bold text-green-600">
              {Math.round(data.response_rate || 83)}%
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2 p-3 bg-yellow-50 rounded-lg">
          <Award className="h-5 w-5 text-yellow-600" />
          <div className="flex-1">
            <p className="text-xs text-gray-600">Crisis Hero Program</p>
            <p className="text-sm font-semibold text-gray-800">
              Recognition & Gamification
            </p>
          </div>
        </div>

        <div className="pt-3 border-t border-gray-200">
          <h4 className="text-sm font-semibold text-gray-700 mb-2">Top Responders</h4>
          <div className="space-y-2">
            {[
              { name: 'Dr. Rajesh Mehta', score: 485 },
              { name: 'Dr. Priya Sharma', score: 472 },
              { name: 'Dr. Amit Kumar', score: 458 },
            ].map((staff, idx) => (
              <div key={idx} className="flex items-center justify-between text-sm">
                <div className="flex items-center space-x-2">
                  <span className="text-lg">{idx === 0 ? '🥇' : idx === 1 ? '🥈' : '🥉'}</span>
                  <span className="text-gray-700">{staff.name}</span>
                </div>
                <span className="font-medium text-indigo-600">{staff.score}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
