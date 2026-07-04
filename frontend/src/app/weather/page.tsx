import React from 'react';

export default function WeatherPage() {
  return (
    <div className="p-8 bg-gray-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold mb-8">Weather Intelligence</h1>
      <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
        <p className="text-gray-400">Detailed meteorological data will be displayed here.</p>
        <div className="mt-4 p-4 bg-gray-900 rounded border border-gray-700">
          <pre className="text-sm">
{`{
  "location": "Colombo",
  "condition": "Heavy Rain",
  "temperature_celsius": 28,
  "warnings": ["Potential Flash Floods in low-lying areas"]
}`}
          </pre>
        </div>
      </div>
    </div>
  );
}
