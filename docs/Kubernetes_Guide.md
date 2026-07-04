# Kubernetes Deployment Guide

Ceylon Sentinel AI is fully orchestrated via Kubernetes, designed for cloud-agnostic deployment (AWS EKS, GCP GKE, Azure AKS, or bare-metal).

## Architecture
- **Namespace**: `ceylon-sentinel` ensures logical isolation.
- **Compute**: Stateless `Deployments` for Backend (FastAPI) and Frontend (Next.js).
- **Stateful**: `StatefulSets` for PostgreSQL (relational DB) and Qdrant (Vector DB).
- **Caching**: Single-replica `Deployment` for Redis (can be scaled via Redis Sentinel).
- **Autoscaling**: `HorizontalPodAutoscaler` attached to the Backend deployment targeting 70% CPU utilization.
- **Ingress**: NGINX Ingress controller for SSL termination and request routing (`app.ceylonsentinel.ai` and `api.ceylonsentinel.ai`).

## Deployment Steps
1. Apply Namespace: `kubectl apply -f deployment/kubernetes/namespace.yaml`
2. Apply Configs/Secrets: `kubectl apply -f deployment/kubernetes/configmaps.yaml -f deployment/kubernetes/secrets.yaml`
3. Apply Stateful resources: `kubectl apply -f deployment/kubernetes/postgres.yaml -f deployment/kubernetes/qdrant.yaml -f deployment/kubernetes/redis.yaml`
4. Apply Compute resources: `kubectl apply -f deployment/kubernetes/backend.yaml -f deployment/kubernetes/frontend.yaml`
5. Expose via Ingress: `kubectl apply -f deployment/kubernetes/ingress.yaml`

## Health Checks
All compute pods are instrumented with `livenessProbe` and `readinessProbe` to guarantee zero-downtime rolling updates.
