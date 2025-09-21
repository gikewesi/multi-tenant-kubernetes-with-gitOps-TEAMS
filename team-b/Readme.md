# Team B – Security & Governance

## Purpose
Team B enforces security and governance across the cluster.  
They own policy management and compliance reporting.

## Responsibilities
- Define and apply Kyverno policies.
- Deploy Policy Reporter UI for visibility into policy violations.
- Manage governance namespace (`governance`).
- Enforce restrictions such as image policies, network restrictions, and Pod Security Standards.

## Folder Contents
- `kyverno-policies/` → Example policy YAMLs.  
- `policy-reporter/` → Helm chart values for Policy Reporter.  
- `namespace.yaml` → Namespace definition for governance tools.  

## Interactions
- Policies validate deployments from Team A.  
- Violations are reported via Policy Reporter.  
- Collaborates with Team C to generate compliance dashboards.
