import type { Metadata } from "next";
import { Orbitron, Rajdhani } from "next/font/google";
import "./globals.css";
import Scene3D from "../components/Scene3D";

const orbitron = Orbitron({
  variable: "--font-orbitron",
  subsets: ["latin"],
});

const rajdhani = Rajdhani({
  weight: ["300", "400", "500", "600", "700"],
  variable: "--font-rajdhani",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Ceylon Sentinel AI | 2050",
  description: "Next Generation Holographic AI Decision Engine",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${orbitron.variable} ${rajdhani.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-black text-cyan-50 font-sans relative overflow-x-hidden">
        <Scene3D />
        
        {/* Futuristic Cyber Nav */}
        <nav className="bg-black/60 backdrop-blur-xl border-b border-cyan-900/50 p-4 sticky top-0 z-50 shadow-[0_0_20px_rgba(0,240,255,0.2)]">
          <div className="max-w-6xl mx-auto flex gap-8 font-bold tracking-widest uppercase text-sm">
            <a href="/dashboard" className="hover:text-cyan-400 text-cyan-200 transition-colors drop-shadow-[0_0_8px_rgba(0,240,255,0.8)]">Dashboard</a>
            <a href="/chat" className="hover:text-cyan-400 text-cyan-200 transition-colors drop-shadow-[0_0_8px_rgba(0,240,255,0.8)]">AI Core</a>
            <a href="/weather" className="hover:text-cyan-400 text-cyan-200 transition-colors drop-shadow-[0_0_8px_rgba(0,240,255,0.8)]">Weather</a>
            <a href="/news" className="hover:text-cyan-400 text-cyan-200 transition-colors drop-shadow-[0_0_8px_rgba(0,240,255,0.8)]">Intel</a>
          </div>
        </nav>
        
        <main className="flex-1 relative z-10">
          {children}
        </main>
      </body>
    </html>
  );
}
