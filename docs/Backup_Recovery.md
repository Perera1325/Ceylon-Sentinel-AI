# Backup & Disaster Recovery

## Backup Strategy
- **PostgreSQL**: Automated `pg_dump` jobs configured via CronJobs to stream encrypted backups to AWS S3 / Cloud Storage daily.
- **Qdrant**: Volume snapshots of the PersistentVolumeClaim (PVC). For application-level backups, the `qdrant-client` snapshot API is triggered weekly.
- **Configurations**: Stored entirely as code (GitOps) via Kubernetes ConfigMaps and GitHub repositories.

## Disaster Recovery Procedure
1. **Total Cluster Failure**: 
   - Deploy new cluster.
   - Apply base Kubernetes manifests.
   - Restore PVCs from cloud snapshots.
   - Restart pods.
2. **Database Corruption**:
   - Spin down FastAPI backend pods to stop incoming writes.
   - Drop the current database schema.
   - Restore from the most recent S3 `pg_dump` artifact.
   - Spin up FastAPI backend pods.
3. **Agent / LLM Provider Outage**:
   - The platform gracefully degrades by utilizing cached historical policies in the RAG Vector DB. The `ConfidenceEngine` will flag the LLM output as low-confidence.
