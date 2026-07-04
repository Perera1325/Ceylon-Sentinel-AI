import { useState, useEffect } from 'react';

export type SSEEvent = {
  event: string;
  data: any;
};

export function useSSE(url: string | null) {
  const [messages, setMessages] = useState<SSEEvent[]>([]);
  const [error, setError] = useState<Error | null>(null);
  const [isComplete, setIsComplete] = useState<boolean>(false);

  useEffect(() => {
    if (!url) return;
    
    setIsComplete(false);
    setMessages([]);
    setError(null);
    
    const eventSource = new EventSource(url);

    eventSource.addEventListener('progress', (e) => {
      try {
        const data = JSON.parse(e.data);
        setMessages((prev) => [...prev, { event: 'progress', data }]);
      } catch (err) {
        console.error("Failed to parse progress event data", err);
      }
    });

    eventSource.addEventListener('complete', (e) => {
      try {
        const data = JSON.parse(e.data);
        setMessages((prev) => [...prev, { event: 'complete', data }]);
        setIsComplete(true);
        eventSource.close();
      } catch (err) {
        console.error("Failed to parse complete event data", err);
      }
    });

    eventSource.onerror = (err) => {
      console.error('EventSource failed:', err);
      setError(new Error('EventSource failed'));
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, [url]);

  return { messages, error, isComplete };
}
