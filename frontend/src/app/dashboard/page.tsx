'use client';
import React, { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import { Activity, Server, Database, BrainCircuit } from 'lucide-react';
import 'leaflet/dist/leaflet.css';

// Dynamically import the Map component to avoid SSR issues with Leaflet
const MapComponent = dynamic(() => import('../../components/Map'), { 
  ssr: false,
  loading: () => <div className="h-96 bg-gray-800 rounded-xl flex items-center justify-center animate-pulse">Loading Map...</div>
});

export default function Dashboard() {
  const [stats, setStats] = useState({
    agents_active: 4,
    workflows_run: 124,
    avg_latency: '1.2s',
    system_health: 'Healthy'
  });

  return (
    <div className="p-8 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-8">System Dashboard</h1>
      
      {/* Metrics Row */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-blue-900/50 rounded-lg text-blue-400">
              <BrainCircuit />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Active Agents</p>
              <h3 className="text-2xl font-bold">{stats.agents_active}</h3>
            </div>
          </div>
        </div>
        
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-green-900/50 rounded-lg text-green-400">
              <Activity />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Workflows Run</p>
              <h3 className="text-2xl font-bold">{stats.workflows_run}</h3>
            </div>
          </div>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-purple-900/50 rounded-lg text-purple-400">
              <Server />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Avg Latency</p>
              <h3 className="text-2xl font-bold">{stats.avg_latency}</h3>
            </div>
          </div>
        </div>

        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
          <div className="flex items-center gap-4">
            <div className="p-3 bg-teal-900/50 rounded-lg text-teal-400">
              <Database />
            </div>
            <div>
              <p className="text-gray-400 text-sm">Database</p>
              <h3 className="text-2xl font-bold">{stats.system_health}</h3>
            </div>
          </div>
        </div>
      </div>

      {/* Map Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 bg-gray-800 rounded-xl border border-gray-700 p-1 overflow-hidden h-[500px]">
          <MapComponent />
        </div>
        
        <div className="bg-gray-800 p-6 rounded-xl border border-gray-700 h-[500px] overflow-y-auto">
          <h2 className="text-xl font-bold mb-4">Live Collector Feed</h2>
          
          <div className="space-y-4">
             <div className="bg-gray-900 p-4 rounded-lg border border-gray-700">
               <span className="text-xs bg-red-900/50 text-red-400 px-2 py-1 rounded-full font-bold">WEATHER</span>
               <p className="mt-2 text-sm text-gray-300">Heavy rain detected in Kalutara region. Anomaly score: 0.89</p>
             </div>
             
             <div className="bg-gray-900 p-4 rounded-lg border border-gray-700">
               <span className="text-xs bg-yellow-900/50 text-yellow-400 px-2 py-1 rounded-full font-bold">NEWS</span>
               <p className="mt-2 text-sm text-gray-300">NewsFirst: "Landslide warnings issued for Sabaragamuwa province."</p>
             </div>

             <div className="bg-gray-900 p-4 rounded-lg border border-gray-700">
               <span className="text-xs bg-blue-900/50 text-blue-400 px-2 py-1 rounded-full font-bold">SYSTEM</span>
               <p className="mt-2 text-sm text-gray-300">RAG Vector DB optimized. 1200 new embeddings added.</p>
             </div>
          </div>
        </div>
      </div>
    </div>
  );
}
