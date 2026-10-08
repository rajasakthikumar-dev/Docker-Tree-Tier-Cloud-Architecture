# 🐳 Docker Compose 3-Tier Architecture

## 📌 Project Overview

This project demonstrates a 3-tier web application deployed using Docker Compose.

The application consists of three services: a frontend using Nginx, a backend using Python Flask, and a MySQL database. Docker Compose manages all three containers and their communication.

This project helps demonstrate containerization, service networking, and multi-container application deployment.

## 🏗️ Architecture

The application follows a 3-tier architecture:

1. **Frontend:** Nginx serves the web page.
2. **Backend:** Python Flask handles application requests.
3. **Database:** MySQL stores application data and provides database connectivity.

### Architecture Flow

```text
User Browser
     |
     v
Nginx Frontend (Port 80)
     |
     v
Python Flask Backend (Port 5000)
     |
     v
MySQL Database (Port 3306)