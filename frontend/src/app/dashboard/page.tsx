'use client';
import React, { useState, useEffect } from 'react';
import dynamic from 'next/dynamic';
import { Activity, Server, Database, BrainCircuit, ShieldAlert, CheckCircle, Clock } from 'lucide-react';
import { motion, Variants } from 'framer-motion';
import 'leaflet/dist/leaflet.css';

const MapComponent = dynamic(() => import('../../components/Map'), { 
  ssr: false,
  loading: () => <div className="h-96 bg-gray-800/50 backdrop-blur-md rounded-xl flex items-center justify-center animate-pulse">Loading Map...</div>
});

const containerVariants: Variants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.15 }
  }
};

const itemVariants: Variants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 300, damping: 24 } }
};

export default function Dashboard() {
  const [stats, setStats] = useState({
    agents_active: 4,
    workflows_run: 124,
    avg_latency: '1.2s',
    system_health: 'Healthy'
  });
  
  const [intelligence, setIntelligence] = useState<any>({
    risk: { score: 0, level: 'Low' },
    confidence: { confidence_score: 0.0 },
    timeline: [],
    llmops: { total_tokens: 0, total_cost: 0, average_latency: 0 }
  });

  useEffect(() => {
    // Fetch intelligence telemetry
    const fetchData = async () => {
      try {
        const [riskRes, confRes, timeRes, opsRes] = await Promise.all([
          fetch('http://localhost:8000/api/v1/intelligence/risk'),
          fetch('http://localhost:8000/api/v1/intelligence/confidence'),
          fetch('http://localhost:8000/api/v1/intelligence/timeline'),
          fetch('http://localhost:8000/api/v1/intelligence/llmops')
        ]);
        const risk = await riskRes.json();
        const confidence = await confRes.json();
        const timeline = await timeRes.json();
        const llmops = await opsRes.json();
        
        setIntelligence({ risk, confidence, timeline, llmops });
      } catch (e) {
        console.error("Failed to fetch intelligence", e);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 10000); // Poll every 10s
    return () => clearInterval(interval);
  }, []);

  return (
    <motion.div 
      className="p-8 min-h-[calc(100vh-73px)] text-cyan-50"
      variants={containerVariants}
      initial="hidden"
      animate="show"
    >
      <motion.h1 variants={itemVariants} className="text-4xl font-extrabold mb-10 text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 tracking-tight drop-shadow-[0_0_15px_rgba(0,240,255,0.5)]">
        Intelligence Dashboard
      </motion.h1>
      
      {/* Intelligence & LLMOps Row */}
      <motion.div variants={containerVariants} className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-10">
        {[
          { label: 'Risk Score', value: `${intelligence.risk.score}/100`, sub: intelligence.risk.level, icon: ShieldAlert, color: intelligence.risk.score > 75 ? 'text-red-400' : 'text-cyan-400', bg: 'bg-black/50' },
          { label: 'Confidence', value: `${(intelligence.confidence.confidence_score * 100).toFixed(0)}%`, sub: 'AI Groundedness', icon: CheckCircle, color: 'text-green-400', bg: 'bg-black/50' },
          { label: 'LLM Tokens', value: intelligence.llmops.total_tokens || 0, sub: `Cost: $${(intelligence.llmops.total_cost || 0).toFixed(4)}`, icon: BrainCircuit, color: 'text-purple-400', bg: 'bg-black/50' },
          { label: 'Avg Latency', value: `${(intelligence.llmops.average_latency || 0).toFixed(2)}s`, sub: 'Agent Execution', icon: Activity, color: 'text-teal-400', bg: 'bg-black/50' },
        ].map((stat, i) => (
          <motion.div 
            key={i}
            variants={itemVariants}
            whileHover={{ scale: 1.05, y: -5 }}
            className="bg-black/40 backdrop-blur-xl p-6 rounded-2xl border border-cyan-500/20 shadow-[0_0_20px_rgba(0,240,255,0.1)] hover:border-cyan-400/50 hover:shadow-[0_0_30px_rgba(0,240,255,0.3)] transition-all duration-300 relative overflow-hidden"
          >
            {/* Scanline overlay for cards */}
            <div className="absolute inset-0 z-0 pointer-events-none opacity-20" style={{ backgroundImage: 'linear-gradient(transparent 50%, rgba(0, 240, 255, 0.1) 50%)', backgroundSize: '100% 4px' }}></div>
            
            <div className="flex items-center gap-4 relative z-10">
              <div className={`p-4 rounded-xl ${stat.bg} ${stat.color} shadow-[0_0_15px_currentColor]`}>
                <stat.icon size={28} />
              </div>
              <div>
                <p className="text-cyan-200/70 text-xs font-bold uppercase tracking-widest">{stat.label}</p>
                <h3 className="text-3xl font-black mt-1 font-mono">{stat.value}</h3>
                <p className="text-xs text-cyan-400/50 mt-1 uppercase">{stat.sub}</p>
              </div>
            </div>
          </motion.div>
        ))}
      </motion.div>

      {/* Map & Timeline Section */}
      <motion.div variants={containerVariants} className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <motion.div 
          variants={itemVariants} 
          className="lg:col-span-2 bg-black/40 backdrop-blur-xl rounded-2xl border border-cyan-500/20 shadow-[0_0_20px_rgba(0,240,255,0.1)] p-2 overflow-hidden h-[500px]"
        >
          <div className="h-full w-full rounded-xl overflow-hidden relative z-10">
            <MapComponent />
          </div>
        </motion.div>
        
        <motion.div 
          variants={itemVariants}
          className="bg-black/40 backdrop-blur-xl p-6 rounded-2xl border border-cyan-500/20 shadow-[0_0_20px_rgba(0,240,255,0.1)] h-[500px] overflow-y-auto custom-scrollbar relative"
        >
          <div className="absolute inset-0 z-0 pointer-events-none opacity-10" style={{ backgroundImage: 'linear-gradient(transparent 50%, rgba(0, 240, 255, 0.2) 50%)', backgroundSize: '100% 4px' }}></div>
          
          <h2 className="text-2xl font-bold mb-6 flex items-center gap-2 relative z-10 text-cyan-400 font-mono uppercase tracking-widest">
            <Clock size={20} className="animate-pulse text-cyan-300" />
            Incident Timeline
          </h2>
          
          <div className="space-y-4 relative z-10 border-l border-cyan-500/30 ml-3 pl-4">
             {intelligence.timeline && intelligence.timeline.length > 0 ? intelligence.timeline.map((event: any, i: number) => (
               <motion.div 
                 key={i}
                 initial={{ opacity: 0, x: 20 }}
                 animate={{ opacity: 1, x: 0 }}
                 transition={{ delay: 0.5 + (i * 0.2) }}
                 className="relative"
               >
                 <div className="absolute -left-[21px] top-1.5 w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_10px_#00f0ff]"></div>
                 <span className="text-xs font-mono text-cyan-200/70">{event.timestamp}</span>
                 <span className={`ml-3 text-xs px-2 py-0.5 rounded font-bold border uppercase tracking-widest border-cyan-500/30 bg-cyan-900/30 text-cyan-300`}>
                   {event.source}
                 </span>
                 <p className="mt-1 text-sm text-cyan-50 leading-relaxed font-medium">{event.event}</p>
               </motion.div>
             )) : (
               <div className="text-cyan-500/50 font-mono text-sm">Waiting for incoming telemetry...</div>
             )}
          </div>
        </motion.div>
      </motion.div>
    </motion.div>
  );
}
