# Demo App – Multi-Tenant Kubernetes with GitOps

This is a simple Flask demo application for showcasing multi-tenancy, GitOps deployment via Argo CD, and observability with Prometheus and Grafana.

---

## Purpose

- Provide a visual demo app for Team A to deploy workloads.
- Demonstrate namespace isolation and team ownership.
- Showcase metrics collection for Team C (observability) using Prometheus and Grafana.
- Integrate with Argo CD for GitOps-based deployment and automation.

---

## Teams & Namespaces

| Team       | Namespace  | Purpose / Access |
|-----------|------------|----------------|
| **Team A** | team-a    | Deploy apps, manage workloads; read/write to Argo CD for their apps; read-only access to Grafana dashboards. |
| **Team B** | team-b    | Manage governance/security workloads; full access to governance tools (Kyverno, Policy Reporter); read-only Argo CD and monitoring. |
| **Team C** | team-c    | Observability; full access to Prometheus/Grafana; read-only access to team-a and team-b namespaces for metrics collection. |

---

## Tool Namespaces

| Namespace    | Tools                 | Purpose |
|-------------|----------------------|---------|
| **argocd**   | Argo CD               | GitOps deployment |
| **governance** | Kyverno, Policy Reporter | Security & policy compliance |
| **monitoring** | Prometheus, Grafana | Metrics collection & dashboards |

---

## Features

- **Frontend:** Colorful, centered “Hello Teams!!! 🎉” page with button interaction.
- **Backend:** Flask app serving the frontend and exposing Prometheus metrics at `/metrics`.
- **Metrics:** Scraped by Prometheus, visualized in Grafana dashboards.
- **Deployment:** Dockerized and deployable via Kubernetes with Argo CD.

---

## Deployment

1. Build and push Docker image to ECR.
2. Update image tag in Kubernetes manifests (`deployment.yaml`) with latest commit hash.
3. Apply resources via Argo CD or `kubectl apply -k demo-app/`.
4. Access the app at the ClusterIP/Ingress URL.
5. Prometheus scrapes `/metrics`, Grafana visualizes team dashboards.

---

## Observability

- Metrics endpoint: `/metrics`
- Team C dashboards in Grafana show real-time metrics for apps in team-a and team-b.
- Demonstrates cross-namespace collaboration while maintaining RBAC isolation.

---

## Notes

- Each team has access only to their namespaces and relevant tool namespaces.
- This setup demonstrates a safe multi-tenant Kubernetes environment with proper RBAC.
- Image pull policy, namespace isolation, and Argo CD GitOps workflow are implemented for reproducibility.

