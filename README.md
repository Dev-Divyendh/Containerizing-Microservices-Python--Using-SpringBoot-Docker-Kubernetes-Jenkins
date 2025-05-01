# Extra Credit Project: Student Survey Microservice (SWE 645)

## 🚀 Project Overview

This project, developed by **Dev Divyendh Dhinakaran** and **Tejaswi**, is a Python-based microservice application that captures and manages student survey data. It demonstrates the full development-to-deployment pipeline, including:

- Flask microservice for handling CRUD operations
- Amazon RDS (MySQL) for data persistence
- Docker containerization
- Kubernetes (K3s) deployment on AWS EC2
- CI/CD automation using Jenkins and GitHub

---

## 🧱 Tech Stack

| Layer         | Tool / Framework            |
|---------------|-----------------------------|
| Backend       | Python, Flask               |
| Database      | Amazon RDS (MySQL)          |
| Container     | Docker                      |
| Orchestration | Kubernetes via K3s          |
| CI/CD         | Jenkins                     |
| VCS           | GitHub                      |
| Cloud Infra   | AWS EC2, RDS                |

---

## 🔧 Application Features

- POST /survey – Create a new survey entry
- GET /surveys – Retrieve all surveys
- PUT /survey/<id> – Update a survey entry
- DELETE /survey/<id> – Delete a survey

---

## 🏗️ Architecture & Infrastructure

### 🛠️ Flask Microservice

The app exposes REST APIs for CRUD operations on survey records. It uses:
- Flask
- Flask-SQLAlchemy
- PyMySQL
- .env variables for DB configs

### 🗄️ Amazon RDS

- **Engine**: MySQL
- **Instance Type**: db.t3.micro
- **Public Access**: Enabled
- **Security Group**: Inbound MySQL (3306) from EC2 IP

### 🖥️ EC2 Instance

- **Type**: t2.medium
- **OS**: Ubuntu 24.04
- **Installed**: Docker, Jenkins, K3s

#### Security Group:
- Port 22 – SSH from user IP
- Port 5000 – Flask dev access (optional)
- Port 30036 – Kubernetes NodePort

### 🐳 Docker

- Dockerfile builds the Flask app
- Image pushed to Docker Hub: `devdivyendh10/extra-student-survey`

### ☸️ Kubernetes (K3s)

- Used lightweight `k3s` distro
- Deployment and Service defined in:
  - `deployment.yaml`
  - `service.yaml`

### ⚙️ Jenkins CI/CD

- **Jenkinsfile** stages:
  - Clone code from GitHub
  - Build Docker image
  - Push to Docker Hub
  - Deploy via `kubectl apply`
- Jenkins is installed on EC2 and configured to access Kubernetes via KUBECONFIG

---

## 📂 Repository Structure

```
student-survey-app/
├── app.py
├── models.py
├── config.py
├── requirements.txt
├── .env
├── Dockerfile
├── deployment.yaml
├── service.yaml
└── Jenkinsfile
```

---

## 🌐 Live Demo

- Kubernetes NodePort: `http://<EC2_PUBLIC_IP>:30036`
- API tested using Postman

---

## 🎥 Video Walkthrough

A complete video is included in the submission, showcasing:
- Code walkthrough
- EC2 & RDS setup
- Docker build & push
- Jenkins pipeline execution
- Kubernetes deployment
- Live result validation

---

## 👥 Team Members

- Dev Divyendh Dhinakaran
- Tejaswi

---

## 📘 License

This project is created for academic use (SWE 645 – Extra Credit Assignment). © 2025
