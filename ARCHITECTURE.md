# Architecture Diagram

```mermaid
flowchart LR

User --> Ingress

Ingress --> ServiceBackend
ServiceBackend --> BackendPods

BackendPods --> ServiceDB
ServiceDB --> Postgres

Postgres --> PVC

GitHub --> GitHubActions
GitHubActions --> DockerHub
GitHubActions --> HelmValues

HelmValues --> ArgoCD
ArgoCD --> KubernetesCluster

Prometheus --> BackendPods
Grafana --> Prometheus
