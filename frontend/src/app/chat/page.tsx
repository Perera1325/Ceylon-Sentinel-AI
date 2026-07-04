'use client';
import React, { useState } from 'react';
import { useSSE } from '../../hooks/useSSE';
import { Send, Activity, ShieldAlert, Cpu } from 'lucide-react';
import { motion, AnimatePresence, Variants } from 'framer-motion';

export default function ChatPage() {
  const [query, setQuery] = useState('');
  const [submittedQuery, setSubmittedQuery] = useState<string | null>(null);
  const [sseUrl, setSseUrl] = useState<string | null>(null);
  const { messages, isComplete } = useSSE(sseUrl);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    
    const sessionId = Math.random().toString(36).substring(7);
    const url = `http://localhost:8000/api/v1/chat?user_query=${encodeURIComponent(query)}&session_id=${sessionId}`;
    
    setSubmittedQuery(query);
    setSseUrl(url);
    setQuery('');
  };

  const containerVariants: Variants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const itemVariants: Variants = {
    hidden: { opacity: 0, y: 10 },
    show: { opacity: 1, y: 0 }
  };

  const isStreaming = !!sseUrl && !isComplete;

  return (
    <motion.div 
      className="max-w-4xl mx-auto p-4 md:p-8 min-h-[calc(100vh-73px)] flex flex-col"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <motion.div 
        className="mb-8 text-center"
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ delay: 0.2, type: "spring" }}
      >
        <h1 className="text-4xl font-extrabold mb-3 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">AI Decision Engine</h1>
        <p className="text-gray-400 font-medium">Ask questions to trigger the multi-agent orchestration workflow.</p>
      </motion.div>

      {/* Main Chat Box - Glassmorphism */}
      <div className="flex-1 bg-gray-800/40 backdrop-blur-xl rounded-3xl border border-white/10 shadow-[0_8px_32px_0_rgba(0,0,0,0.37)] flex flex-col overflow-hidden mb-6 relative">
        <div className="flex-1 overflow-y-auto p-6 space-y-4 custom-scrollbar">
          <AnimatePresence>
            {!submittedQuery ? (
              <motion.div 
                initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
                className="h-full flex flex-col items-center justify-center text-gray-500 gap-4"
              >
                <div className="p-4 bg-gray-800/50 rounded-full border border-gray-700 shadow-inner">
                   <Cpu size={48} className="text-blue-500/50 animate-pulse" />
                </div>
                <p className="text-lg">System idle. Awaiting query...</p>
              </motion.div>
            ) : (
              <motion.div variants={containerVariants} initial="hidden" animate="show" className="space-y-4">
                
                {/* User Message */}
                <motion.div variants={itemVariants} className="bg-blue-900/30 border border-blue-800/50 p-4 rounded-xl mb-6 shadow-inner">
                  <span className="font-bold text-blue-400">User:</span> <span className="text-blue-100">{submittedQuery}</span>
                </motion.div>

                {/* Workflow Messages */}
                {messages.map((msg, idx) => {
                  if (msg.event === 'progress') {
                    return (
                      <motion.div 
                        key={idx}
                        variants={itemVariants}
                        layout
                        className="flex items-center gap-3 text-sm text-gray-400 bg-gray-900/50 p-4 rounded-xl border border-white/5"
                      >
                        <Cpu size={16} className="text-yellow-500 animate-pulse" />
                        <span className="font-semibold text-gray-300 px-2 py-1 bg-gray-800 rounded">{msg.data.agent}</span>
                        <span>{msg.data.status}</span>
                      </motion.div>
                    );
                  }
                  
                  if (msg.event === 'complete') {
                    const final = msg.data;
                    return (
                      <motion.div 
                        key={idx}
                        variants={itemVariants}
                        layout
                        className="mt-8 bg-gray-900/80 backdrop-blur-md border border-green-500/30 p-6 rounded-2xl shadow-[0_0_20px_rgba(34,197,94,0.1)]"
                      >
                        <div className="flex justify-between items-start mb-6">
                          <div className="flex items-center gap-3">
                            <ShieldAlert size={28} className={final.risk_level === 'HIGH' ? 'text-red-500' : 'text-green-500'} />
                            <h2 className="text-2xl font-black bg-clip-text text-transparent bg-gradient-to-r from-green-400 to-emerald-600">Policy Report</h2>
                          </div>
                          <div className="bg-green-900/40 text-green-300 font-bold px-4 py-1.5 rounded-full text-sm border border-green-500/50 shadow-inner">
                            Confidence: {(final.confidence * 100).toFixed(0)}%
                          </div>
                        </div>
                        
                        <div className="prose prose-invert max-w-none">
                          <pre className="whitespace-pre-wrap font-sans text-gray-300 text-sm leading-relaxed p-4 bg-gray-950/50 rounded-xl border border-white/5">
                            {final.answer}
                          </pre>
                        </div>
                      </motion.div>
                    );
                  }
                  return null;
                })}

                {/* Loading indicator */}
                {isStreaming && (
                  <motion.div 
                    initial={{ opacity: 0 }} animate={{ opacity: 1 }}
                    className="flex items-center gap-3 text-blue-400 p-4 bg-blue-900/10 rounded-xl border border-blue-500/20 w-max"
                  >
                    <Activity size={18} className="animate-spin" />
                    <span className="font-medium animate-pulse">Processing workflow...</span>
                  </motion.div>
                )}
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* Input Area */}
        <div className="p-4 bg-gray-900/60 backdrop-blur-md border-t border-white/10">
          <form onSubmit={handleSubmit} className="flex gap-4">
            <input 
              type="text" 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              disabled={isStreaming}
              placeholder="e.g. What are the major risks in Sri Lanka today?"
              className="flex-1 bg-gray-800/80 text-white rounded-xl px-5 py-4 border border-gray-600 focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 disabled:opacity-50 transition-all shadow-inner font-medium"
            />
            <motion.button 
              type="submit" 
              disabled={isStreaming || !query.trim()}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white px-8 rounded-xl font-bold flex items-center gap-2 disabled:opacity-50 transition-all shadow-[0_0_20px_rgba(79,70,229,0.4)] disabled:shadow-none"
            >
              {isStreaming ? (
                <><Activity className="animate-spin" size={20}/> Analyzing</>
              ) : (
                <><Send size={20} /> Analyze</>
              )}
            </motion.button>
          </form>
        </div>
      </div>
    </motion.div>
  );
}
