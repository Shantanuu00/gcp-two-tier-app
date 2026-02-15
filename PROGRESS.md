# DevOps Project Progress Log

## Challenges Faced & Solutions

### 1. Metrics Server Not Ready
Problem:
kubectl top returned <unknown>

Solution:
Enabled metrics-server addon in Minikube.

---

### 2. Docker Image Not Updating
Problem:
Old image still running.

Solution:
Used SHA tagging and automated updates via GitHub Actions.

---

### 3. ArgoCD OutOfSync
Problem:
Deployment showed OutOfSync due to auto-scaled replicas.

Solution:
Used ignoreDifferences for replicas and restartedAt annotation.

---

### 4. Database Connectivity Issues
Problem:
Backend couldn't connect to DB.

Solution:
Fixed ConfigMap and Secret environment variables.

---

### 5. Understanding Kubernetes Concepts
Learned:
- Pods vs Containers
- Services for networking
- Ingress for routing
- HPA for scaling
- PVC for storage

---

## Key Learnings

- Kubernetes is a scheduler, not a runtime
- Docker runs containers, Kubernetes manages them
- GitOps ensures desired state is maintained
- Observability is critical in production

---

## Outcome

Built a production-style Kubernetes app with CI/CD and GitOps workflow.

