import React from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import L from 'leaflet';

// Fix Leaflet's default icon path issues in Next.js
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

const center: [number, number] = [7.8731, 80.7718]; // Sri Lanka center

export default function Map() {
  return (
    <MapContainer center={center} zoom={7} style={{ height: '100%', width: '100%' }}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      
      {/* Mock Event: Kalutara Floods */}
      <Marker position={[6.5854, 79.9607]}>
        <Popup>
          <b>Kalutara</b> <br /> Heavy Flooding <br /> Risk: HIGH
        </Popup>
      </Marker>
      
      {/* Mock Event: Ratnapura Landslide */}
      <Circle center={[6.6828, 80.3992]} pathOptions={{ fillColor: 'red', color: 'red' }} radius={15000}>
        <Popup>
          <b>Ratnapura</b> <br /> Landslide Warning Zone <br /> Risk: CRITICAL
        </Popup>
      </Circle>
    </MapContainer>
  );
}
