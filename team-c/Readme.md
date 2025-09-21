# Team C – Observability Team

## Purpose
Team C ensures the cluster and workloads are observable.  
They handle monitoring, metrics, and visualization.

## Responsibilities
- Deploy Prometheus for metrics collection.
- Deploy Grafana for dashboards and visualization.
- Manage monitoring namespace (`monitoring`).
- Integrate alerts and dashboards for Team A and B workloads.

## Folder Contents
- `prometheus/` → Helm chart values for Prometheus.  
- `grafana/` → Helm chart values for Grafana.  
- `namespace.yaml` → Namespace definition for observability tools.  

## Interactions
- Prometheus scrapes application and system metrics.  
- Grafana displays dashboards for apps (Team A) and policies (Team B).  
- Works with Argo CD for GitOps-managed deployments.
