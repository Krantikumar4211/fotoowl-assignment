# Foto Owl – Scalable Image Import System

This project is a scalable, multi-service backend system designed to import images from a public Google Drive folder, store them in cloud object storage, and persist image metadata in a SQL database.

The system is built as part of the Foto Owl AI Junior Backend Developer assignment and follows cloud-ready, production-style architecture principles.

---

## 🚀 Live Demo
🔗 Working Site URL: (to be added after deployment)

---

## 🧠 Architecture Overview

The system follows a **multi-service architecture** to ensure scalability, fault tolerance, and high throughput.

### Services:
- **Frontend** – Simple UI to trigger imports and view images
- **API Service** – Handles requests and job orchestration
- **Worker Service** – Processes image imports asynchronously
- **Redis Queue** – Manages background jobs
- **PostgreSQL** – Stores image metadata
- **Object Storage** – AWS S3 / MinIO compatible storage

---

## 🏗️ Service Breakdown

### Frontend
- Accepts Google Drive folder URL
- Displays imported images
- Built with React

### API Service
- `POST /import/google-drive`
- `GET /images`
- Pushes import jobs to queue
- Built with FastAPI (Python)

### Worker Service
- Fetches images from Google Drive
- Uploads images to cloud storage
- Stores metadata in SQL database
- Built with Python

---

## 📦 Image Metadata Stored

- Image name
- Google Drive file ID
- File size
- MIME type
- Cloud storage path
- Source (Google Drive)

---

## ⚙️ Tech Stack

- **Backend:** Python, FastAPI
- **Worker:** Python
- **Database:** PostgreSQL
- **Queue:** Redis
- **Storage:** AWS S3 / MinIO
- **Frontend:** React
- **Containerization:** Docker & Docker Compose

---

## 📈 Scalability Considerations

- Background job processing using Redis queue
- Worker services can scale independently
- API remains responsive during large imports
- Designed to support 10,000+ images per import

---

## 🐳 Running Locally (Coming Soon)

```bash
docker-compose up --build
