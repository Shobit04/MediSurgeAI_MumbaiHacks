'use client';

import { Activity, Heart, Bell } from 'lucide-react';

export default function Header() {
  return (
    <header className="bg-gradient-to-r from-blue-600 to-blue-800 text-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <div className="bg-white p-2 rounded-lg">
              <Heart className="h-8 w-8 text-red-500" />
            </div>
            <div>
              <h1 className="text-3xl font-bold">MediSurge AI</h1>
              <p className="text-blue-100 text-sm">
                Healthcare Crisis Management System
              </p>
            </div>
          </div>
          
          <div className="flex items-center space-x-6">
            <div className="flex items-center space-x-2 bg-blue-700 px-4 py-2 rounded-lg">
              <Activity className="h-5 w-5 text-green-400 animate-pulse" />
              <span className="text-sm font-medium">System Active</span>
            </div>
            
            <button className="relative p-2 rounded-lg hover:bg-blue-700 transition-colors">
              <Bell className="h-6 w-6" />
              <span className="absolute top-1 right-1 h-2 w-2 bg-red-500 rounded-full"></span>
            </button>
          </div>
        </div>
        
        <div className="mt-4 grid grid-cols-4 gap-4 text-center">
          <div className="bg-blue-700 bg-opacity-50 rounded-lg p-3">
            <p className="text-xs text-blue-100">Prediction Accuracy</p>
            <p className="text-2xl font-bold">87.3%</p>
          </div>
          <div className="bg-blue-700 bg-opacity-50 rounded-lg p-3">
            <p className="text-xs text-blue-100">Active Agents</p>
            <p className="text-2xl font-bold">8/8</p>
          </div>
          <div className="bg-blue-700 bg-opacity-50 rounded-lg p-3">
            <p className="text-xs text-blue-100">System Uptime</p>
            <p className="text-2xl font-bold">99.8%</p>
          </div>
          <div className="bg-blue-700 bg-opacity-50 rounded-lg p-3">
            <p className="text-xs text-blue-100">Response Time</p>
            <p className="text-2xl font-bold">3.2h</p>
          </div>
        </div>
      </div>
    </header>
  );
}
