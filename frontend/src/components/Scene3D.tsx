'use client';
import { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Sphere, MeshDistortMaterial, Stars, Line } from '@react-three/drei';
import * as THREE from 'three';

function HolographicEarth() {
  const meshRef = useRef<THREE.Mesh>(null);
  
  useFrame((state, delta) => {
    if (meshRef.current) {
      meshRef.current.rotation.y += delta * 0.1;
      meshRef.current.rotation.x += delta * 0.05;
    }
  });

  return (
    <group>
      {/* Outer Glow Sphere */}
      <Sphere ref={meshRef} args={[2.2, 64, 64]}>
        <meshBasicMaterial 
          color="#00f0ff" 
          wireframe 
          transparent 
          opacity={0.15} 
          blending={THREE.AdditiveBlending}
        />
      </Sphere>
      
      {/* Inner Core Distorted */}
      <Sphere args={[1.8, 32, 32]}>
        <MeshDistortMaterial 
          color="#0044ff"
          attach="material"
          distort={0.4}
          speed={2}
          roughness={0}
          transparent
          opacity={0.4}
        />
      </Sphere>
    </group>
  );
}

export default function Scene3D() {
  return (
    <div className="absolute inset-0 z-0 bg-black pointer-events-none">
      <Canvas camera={{ position: [0, 0, 6], fov: 45 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={2} color="#00f0ff" />
        <Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
        <HolographicEarth />
      </Canvas>
      {/* Scanline Overlay */}
      <div className="absolute inset-0 z-10 pointer-events-none opacity-20" style={{
        backgroundImage: 'linear-gradient(transparent 50%, rgba(0, 240, 255, 0.25) 50%)',
        backgroundSize: '100% 4px'
      }}></div>
      
      {/* Vignette */}
      <div className="absolute inset-0 z-20 pointer-events-none" style={{
        background: 'radial-gradient(circle at center, transparent 0%, #000 100%)'
      }}></div>
    </div>
  );
}
