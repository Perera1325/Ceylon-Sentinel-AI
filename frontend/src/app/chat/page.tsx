import React, { useState } from 'react';
import { useSSE } from '../hooks/useSSE';
import { Send, Activity, ShieldAlert, Cpu } from 'lucide-react';

export default function ChatPage() {
  const [query, setQuery] = useState('');
  const [submittedQuery, setSubmittedQuery] = useState<string | null>(null);
  const [sseUrl, setSseUrl] = useState<string | null>(null);
  const { messages, isComplete } = useSSE(sseUrl);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query) return;
    
    // In our backend, POST /api/v1/chat returns the SSE stream directly.
    // However, EventSource only supports GET. 
    // To support POST with EventSource, we might need a fetch workaround, 
    // or just change the backend endpoint to GET with query params for simplicity.
    // Let's use a GET workaround by encoding the query in the URL for the SSE stream.
    
    const sessionId = Math.random().toString(36).substring(7);
    // Note: The FastAPI backend expects POST right now. I'll need to update it to support GET or use fetch polyfill.
    // Assuming backend will be updated to GET for EventSource:
    const url = `http://localhost:8000/api/v1/chat?user_query=${encodeURIComponent(query)}&session_id=${sessionId}`;
    
    setSubmittedQuery(query);
    setSseUrl(url);
    setQuery('');
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-8 text-blue-400">AI Decision Engine</h1>
      
      <div className="flex-1 overflow-y-auto mb-6 bg-gray-800 rounded-lg p-6 shadow-xl border border-gray-700">
        {!submittedQuery && (
          <div className="flex items-center justify-center h-full text-gray-500">
            <p>Ask a question to initiate the LangGraph workflow...</p>
          </div>
        )}

        {submittedQuery && (
          <div className="mb-6">
            <div className="bg-blue-900/30 border border-blue-800 p-4 rounded-lg mb-6">
              <span className="font-bold text-blue-400">User:</span> {submittedQuery}
            </div>
            
            <div className="space-y-4">
              {messages.map((msg, idx) => {
                if (msg.event === 'progress') {
                  return (
                    <div key={idx} className="flex items-center gap-3 text-sm text-gray-400 bg-gray-900/50 p-3 rounded">
                      <Cpu size={16} className="text-yellow-500 animate-pulse" />
                      <span className="font-semibold text-gray-300">{msg.data.agent}</span>
                      <span>{msg.data.status}</span>
                    </div>
                  );
                }
                
                if (msg.event === 'complete') {
                  const final = msg.data;
                  return (
                    <div key={idx} className="mt-8 bg-gray-900 border border-gray-700 p-6 rounded-xl shadow-2xl">
                      <div className="flex justify-between items-start mb-6">
                        <div className="flex items-center gap-2">
                          <ShieldAlert className={final.risk_level === 'HIGH' ? 'text-red-500' : 'text-green-500'} />
                          <h2 className="text-xl font-bold">Policy Report</h2>
                        </div>
                        <div className="bg-gray-800 px-3 py-1 rounded-full text-sm border border-gray-600">
                          Confidence: {(final.confidence * 100).toFixed(0)}%
                        </div>
                      </div>
                      
                      <div className="prose prose-invert max-w-none">
                        <pre className="whitespace-pre-wrap font-sans text-gray-300">
                          {final.answer}
                        </pre>
                      </div>
                    </div>
                  );
                }
                return null;
              })}
              
              {sseUrl && !isComplete && (
                <div className="flex items-center gap-2 text-blue-400 p-4">
                  <Activity size={18} className="animate-spin" />
                  <span>Processing workflow...</span>
                </div>
              )}
            </div>
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="flex gap-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. What are the major risks in Sri Lanka today?"
          className="flex-1 bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={!!sseUrl && !isComplete}
        />
        <button
          type="submit"
          disabled={!query || (!!sseUrl && !isComplete)}
          className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 transition-colors px-6 py-3 rounded-lg flex items-center gap-2 font-semibold"
        >
          <span>Analyze</span>
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}
