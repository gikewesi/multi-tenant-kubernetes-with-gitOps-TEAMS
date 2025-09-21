# Team A – Application Team

## Purpose
Team A is responsible for application workloads running on the EKS cluster.  
They own namespaces, Helm charts, and demo apps used to showcase tenant isolation, GitOps, and security policies.

## Responsibilities
- Deploy demo applications using Helm and Argo CD.
- Manage application namespaces (`argocd`).
- Test multi-tenancy features such as network policies and namespace isolation.

## Folder Contents
- `templates/` → Helm templates for apps.  
- `values.yaml` → Configuration values for deployments.  
- `namespace.yaml` → Namespace definition for Team A apps.  

## Interactions
- Argo CD syncs this folder to deploy workloads.  
- Kyverno policies from Team B apply to ensure compliance.  
- Metrics from apps are scraped by Prometheus (Team C).
