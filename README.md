# 🚀 Student Management System - DevOps Project

This project is a Django-based Student Management System designed with a complete DevOps pipeline. It demonstrates how to automate the build, test, and deployment process using modern DevOps tools.

---

## 📌 Project Overview

The application manages student records and is fully containerized and deployed using a CI/CD pipeline.

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Containerization: Docker
- CI/CD: Jenkins
- Code Quality: SonarQube
- Infrastructure: Terraform
- Orchestration: Kubernetes
- Cloud: AWS (EC2 / EKS)

---

## ⚙️ Features

- Student record management
- Dockerized application
- Automated CI/CD pipeline
- Code quality analysis using SonarQube
- Infrastructure as Code using Terraform
- Kubernetes deployment support

---

## 🔄 CI/CD Pipeline Flow

1. Code pushed to Git repository
2. Jenkins triggers pipeline
3. SonarQube performs code analysis
4. Docker image is built
5. Image pushed to DockerHub
6. Deployment using Kubernetes (via Terraform)

---

## 🐳 Docker Setup

Build image:

```bash
docker build -t student-management .
