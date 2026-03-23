# Student Management Deployment Guide

## 1) Docker (Local Validation)

```bash
docker compose up --build -d
docker compose logs -f
```

App URL: `http://localhost:8000`

---

## 2) AWS Prerequisites

- AWS account with ECR + EKS access
- EKS cluster created
- Ingress Controller installed on EKS (example: NGINX Ingress)
- Jenkins agent with:
  - Docker
  - AWS CLI
  - kubectl

---

## 3) Update Placeholders

### `Jenkinsfile`
- `AWS_ACCOUNT_ID`
- `AWS_REGION`
- `EKS_CLUSTER_NAME`

### `k8s/deployment.yaml`
- ECR image path:
  - `<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/student-management:latest`
- `DJANGO_CSRF_TRUSTED_ORIGINS` (set your real domain)

### `k8s/ingress.yaml`
- `student.example.com` to your real domain

---

## 4) Jenkins Setup

Create AWS credentials in Jenkins:
- **Kind**: AWS Credentials
- **Credentials ID**: `aws-jenkins-creds`

Then create a Pipeline job pointing to this repo.

---

## 5) Kubernetes Deploy (Manual First-Time)

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

Check:

```bash
kubectl get pods -n student-management
kubectl get svc -n student-management
kubectl get ingress -n student-management
```

---

## 6) CI/CD Flow

On every Jenkins build:
1. Docker image build
2. Push to ECR (`latest` + build tag)
3. Apply K8s manifests
4. Update deployment image
5. Wait for rollout success

---

## 7) Environment Variables Used

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`

Set secure values in production.
