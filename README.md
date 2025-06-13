# 🖥️ Service Health Dashboard - CI/CD with Jenkins, Docker, Flask on AWS EC2

A beginner-friendly DevOps project to build and deploy a system health monitoring dashboard using **Flask**, **Docker**, and **Jenkins** on a **Free Tier AWS EC2 instance**.

This project helps you learn the basics of cloud setup, containerization, CI/CD automation, and monitoring.

---

## 🚀 Project Overview

This project builds a real-time **Service Health Dashboard** using:

- **Flask** (with `psutil` and `APScheduler`) for system metrics
- **Chart.js** for frontend visualization
- **Docker** to containerize the app
- **Jenkins** to automate CI/CD
- **GitHub Webhooks** for push-triggered deployments (optional)
- **AWS EC2 (Free Tier)** as the hosting environment

---

## 🔧 Tech Stack

| Tool         | Purpose                      |
|--------------|------------------------------|
| Flask        | Web framework                |
| psutil       | System resource tracking     |
| APScheduler  | Task scheduling              |
| Chart.js     | Chart rendering (Frontend)   |
| Docker       | Containerization             |
| Jenkins      | CI/CD automation             |
| GitHub       | Source control               |
| AWS EC2      | Cloud hosting                |

---

## 🧩 Project Phases

### ✅ Phase 1: EC2 Setup

- Launch **EC2 t2.micro (Ubuntu)**
- Install: Python3, pip, Flask, Docker, Jenkins, Git
- Open ports: `5000` (Flask), `8080` (Jenkins)

### ✅ Phase 2: Flask App

- Creating a basic Flask app using:
  - `psutil` for CPU, RAM stats
  - `APScheduler` to poll every 1 minute
- Display metrics using Chart.js dashboard

### ✅ Phase 3: Dockerization

- Write `Dockerfile` to containerize the Flask app
- Expose port `5000` and run container inside EC2

### ✅ Phase 4: Jenkins CI/CD

- Install Jenkins and configure a **Pipeline Job**
- Add `Jenkinsfile` with stages:
  - Clone GitHub repo
  - Build Docker image
  - Run container
- Setup **GitHub Webhook** for push-triggered deployment (optional)

### ✅ Phase 5: Monitoring

- Add alerting inside Flask app (e.g., CPU > 70%, RAM > 70%)
- *(Optional)* Use **AWS CloudWatch Agent** for deeper system metrics (not included in this project)

---

## 📋 Completion Checklist

| Feature                                  | Status |
|------------------------------------------|--------|
| Flask + Chart.js dashboard               | ✅     |
| Dockerized Flask App                     | ✅     |
| Jenkins CI/CD Pipeline                   | ✅     |
| Runs on AWS Free Tier (Single EC2)       | ✅     |

---

## 📷 Demo Screenshot

![image](https://github.com/user-attachments/assets/ad80fe7a-d43d-405d-a139-f31c29b5ec09)
![image](https://github.com/user-attachments/assets/4599fe6e-598e-4d6d-acb1-2438b44f691d)



