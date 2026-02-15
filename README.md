# GCP-Style Two-Tier DevOps Application on Kubernetes

A production-style **two-tier web application** deployed on Kubernetes using DevOps best practices.

This project demonstrates containerization, orchestration, CI/CD, GitOps, autoscaling, and observability — similar to real-world cloud deployments.

---

## 🚀 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **Package Manager:** Helm
- **CI/CD:** GitHub Actions
- **GitOps:** ArgoCD
- **Monitoring:** Prometheus + Grafana
- **Cloud-ready design:** Compatible with GKE/EKS/AKS

---

## 🏗 Architecture

User → Ingress → Service → Backend Pod → PostgreSQL Pod → PVC Storage

Key Kubernetes resources:

- Deployment (backend, postgres)
- Service (ClusterIP, NodePort)
- Ingress (NGINX)
- ConfigMap (DB configs)
- Secret (DB password)
- PersistentVolumeClaim (database storage)
- HPA (Horizontal Pod Autoscaler)

---

## ⚙️ Features Implemented

✅ Dockerized FastAPI application  
✅ PostgreSQL with persistent storage  
✅ Helm-based deployment  
✅ Kubernetes Ingress routing (api.local)  
✅ Horizontal Pod Autoscaling  
✅ Liveness & Readiness probes  
✅ CI pipeline with GitHub Actions  
✅ Automated image builds & tagging  
✅ GitOps deployment using ArgoCD  
✅ Prometheus metrics endpoint (/metrics)  
✅ Grafana dashboards for observability  

---

## 📦 CI/CD Flow

1. Developer pushes code to GitHub  
2. GitHub Actions:
   - Builds Docker image
   - Tags with commit SHA
   - Pushes to DockerHub
   - Updates Helm values.yaml
3. ArgoCD detects change
4. ArgoCD deploys to Kubernetes automatically

---

## 📊 Monitoring

- Prometheus scrapes metrics from `/metrics`
- Grafana dashboards visualize system metrics
- Node Exporter dashboard integrated

---

## 🧪 API Endpoints

| Endpoint | Purpose |
|--------|--------|
| `/health` | Health check |
| `/db` | DB connectivity test |
| `/db/init` | Initialize table |
| `/db/visit` | Insert record |
| `/db/visits` | Count visits |
| `/metrics` | Prometheus metrics |

---

## 📁 Project Structure
app/
helm/two-tier/
.github/workflows/
monitoring/


---

## 🎯 Learning Goals Achieved

- Kubernetes fundamentals
- GitOps workflow
- Real-world CI/CD pipelines
- Observability stack
- Production-style deployments

---

## 🔮 Future Improvements

- Deploy to GKE
- Add TLS with cert-manager
- Add Redis caching
- Advanced alerting rules

