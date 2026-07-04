'use client';
import React, { useState } from 'react';
import { motion, Variants } from 'framer-motion';
import { Users, Settings, Bell, Shield, Terminal, BrainCircuit, Activity } from 'lucide-react';

const containerVariants: Variants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 }
  }
};

const itemVariants: Variants = {
  hidden: { opacity: 0, x: -20 },
  show: { opacity: 1, x: 0 }
};

export default function AdminDashboard() {
  const [activeTab, setActiveTab] = useState('users');

  const tabs = [
    { id: 'users', label: 'User Management', icon: Users },
    { id: 'security', label: 'Security & RBAC', icon: Shield },
    { id: 'llmops', label: 'LLMOps & Prompts', icon: BrainCircuit },
    { id: 'notifications', label: 'Notifications', icon: Bell },
    { id: 'logs', label: 'Audit Logs', icon: Terminal },
    { id: 'settings', label: 'System Settings', icon: Settings },
  ];

  return (
    <motion.div 
      className="max-w-7xl mx-auto p-4 md:p-8 min-h-[calc(100vh-73px)] text-cyan-50 flex gap-8"
      variants={containerVariants}
      initial="hidden"
      animate="show"
    >
      {/* Sidebar Navigation */}
      <motion.div variants={itemVariants} className="w-64 shrink-0 bg-black/40 backdrop-blur-xl border border-cyan-500/20 rounded-2xl p-4 shadow-[0_0_20px_rgba(0,240,255,0.1)] h-max sticky top-24">
        <h2 className="text-xl font-bold mb-6 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 tracking-wider uppercase font-mono px-4">
          Admin Console
        </h2>
        <nav className="space-y-2">
          {tabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${
                activeTab === tab.id 
                  ? 'bg-cyan-900/40 text-cyan-300 border border-cyan-500/50 shadow-[0_0_15px_rgba(0,240,255,0.2)]' 
                  : 'text-gray-400 hover:bg-gray-900/50 hover:text-cyan-200 border border-transparent'
              }`}
            >
              <tab.icon size={18} />
              <span className="font-medium tracking-wide">{tab.label}</span>
            </button>
          ))}
        </nav>
      </motion.div>

      {/* Main Content Area */}
      <motion.div variants={itemVariants} className="flex-1 bg-black/40 backdrop-blur-xl border border-cyan-500/20 rounded-2xl p-8 shadow-[0_0_20px_rgba(0,240,255,0.1)] relative overflow-hidden">
        {/* Holographic Scanline Overlay */}
        <div className="absolute inset-0 z-0 pointer-events-none opacity-10" style={{ backgroundImage: 'linear-gradient(transparent 50%, rgba(0, 240, 255, 0.2) 50%)', backgroundSize: '100% 4px' }}></div>
        
        <div className="relative z-10">
          {activeTab === 'users' && (
            <div className="space-y-6">
              <div className="flex justify-between items-center mb-8 border-b border-cyan-500/20 pb-4">
                <h3 className="text-3xl font-black text-cyan-400 tracking-wider">User Directory</h3>
                <button className="bg-cyan-600 hover:bg-cyan-500 text-white px-4 py-2 rounded-lg font-bold transition-colors">
                  + Provision User
                </button>
              </div>
              
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse">
                  <thead>
                    <tr className="border-b border-cyan-500/30 text-cyan-500 font-mono uppercase tracking-widest text-sm">
                      <th className="pb-3 px-4">User</th>
                      <th className="pb-3 px-4">Role</th>
                      <th className="pb-3 px-4">Status</th>
                      <th className="pb-3 px-4">Last Login</th>
                      <th className="pb-3 px-4 text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="text-sm">
                    {['admin@ceylonsentinel.ai', 'operator@ceylonsentinel.ai', 'analyst@ceylonsentinel.ai'].map((email, i) => (
                      <tr key={email} className="border-b border-cyan-500/10 hover:bg-cyan-900/20 transition-colors">
                        <td className="py-4 px-4 font-medium">{email}</td>
                        <td className="py-4 px-4">
                          <span className={`px-2 py-1 rounded text-xs font-bold uppercase tracking-wider ${i === 0 ? 'bg-purple-900/50 text-purple-300 border border-purple-500/30' : 'bg-blue-900/50 text-blue-300 border border-blue-500/30'}`}>
                            {i === 0 ? 'Administrator' : i === 1 ? 'Emergency Operator' : 'Analyst'}
                          </span>
                        </td>
                        <td className="py-4 px-4">
                          <div className="flex items-center gap-2 text-green-400">
                            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
                            Active
                          </div>
                        </td>
                        <td className="py-4 px-4 text-cyan-200/50 font-mono">2 mins ago</td>
                        <td className="py-4 px-4 text-right">
                          <button className="text-cyan-400 hover:text-cyan-300 font-bold text-xs uppercase tracking-widest">Edit</button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'security' && (
            <div className="space-y-6">
              <h3 className="text-3xl font-black text-cyan-400 tracking-wider mb-8 border-b border-cyan-500/20 pb-4">Security Policies</h3>
              <div className="bg-cyan-900/20 border border-cyan-500/30 p-6 rounded-xl">
                <h4 className="font-bold text-lg mb-2">Role-Based Access Control (RBAC) Enforced</h4>
                <p className="text-gray-400 text-sm">Strict JWT-based authentication is currently active. Anonymous access to AI core is disabled.</p>
              </div>
            </div>
          )}

          {activeTab !== 'users' && activeTab !== 'security' && (
            <div className="h-96 flex flex-col items-center justify-center text-cyan-500/50">
              <Activity size={48} className="mb-4 animate-pulse opacity-50" />
              <p className="font-mono tracking-widest uppercase text-sm">Module [{activeTab}] Online - Data stream initializing...</p>
            </div>
          )}
        </div>
      </motion.div>
    </motion.div>
  );
}
