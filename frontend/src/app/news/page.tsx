import React from 'react';

export default function NewsPage() {
  return (
    <div className="p-8 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-8">Disaster News Intel</h1>
      <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
        <p className="text-gray-400">Aggregated alerts from multiple news outlets.</p>
        <div className="mt-4 p-4 bg-gray-900 rounded border border-gray-700">
          <pre className="text-sm">
{`[
  {
    "headline": "Severe flooding reported in Kalutara District",
    "source": "NewsFirst",
    "severity": "HIGH"
  },
  {
    "headline": "Landslide warning issued for Ratnapura",
    "source": "AdaDerana",
    "severity": "CRITICAL"
  }
]`}
          </pre>
        </div>
      </div>
    </div>
  );
}
