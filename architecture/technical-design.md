# Technical Design — Smart Rural Service Access Platform (SR-SAP)

## Objective
SR-SAP is an AI + GIS powered offline-first platform designed to improve rural access to services such as health, governance, skill development, and scheme discovery.

---

## 1. System Architecture Overview
The architecture consists of five primary layers:

### **1. Client Layer**
- React Web App / PWA (offline-first)
- Local caching for low-connectivity users
- Geotagging using HTML5 GPS

### **2. API Layer**
- Flask backend (prototype)
- JWT authentication
- Endpoints for:
  - User registration
  - Geotagged reporting
  - AI-based recommendations

### **3. Database Layer**
- PostgreSQL + PostGIS (production)
- SQLite (development/demo)
- Tables:
  - users
  - reports
  - geo_features
  - sync_queue

### **4. GIS Layer**
- GeoJSON + Tiles (Mapbox or tileserver-gl)
- Spatial queries using PostGIS
- Mapping:
  - PHCs
  - Schools
  - Water points
  - Hazard zones

### **5. AI Microservice**
- Lightweight rule-based model (prototype)
- Can be replaced with:
  - OpenAI models
  - Local Llama model
  - Fine-tuned scheme-recommendation model

---

## 2. Data Flow Diagram
User Device (PWA)
↓
Backend API (Flask)
↓
Database (Postgres/PostGIS)
↓
AI Microservice
↓
Admin Dashboard / GIS Map

---

## 3. Offline-First Design
- Local IndexedDB caching  
- Background sync when network returns  
- SMS fallback for critical reports  

---

## 4. Security & Privacy
- JWT-based secure sessions  
- HTTPS recommended for production  
- Geolocation is opt-in  
- No personally identifiable info stored unnecessarily  

---

## 5. Scalability Plan
- API horizontal autoscaling  
- DB read replicas  
- CDN caching for map tiles  
- Queue-based syncing for offline reports  
- Modular microservices for real AI models  

---

## 6. Deployment
**Prototype**: local machine / GitHub Codespaces  
**Production option**:  
- Backend: Docker + Railway / Render  
- Database: Supabase / Neon  
- Maps: Mapbox  
- Frontend: Netlify / Vercel  

---

## 7. Files in This Repo
- `/backend` – Flask app + tests  
- `/frontend` – React/Vite PWA stub  
- `/data` – Sample CSV and GeoJSON  
- `/architecture` – This document  

---
