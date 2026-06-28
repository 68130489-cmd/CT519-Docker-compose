# ML Web Application with Docker Compose

โปรเจกต์นี้เป็นระบบ Web Application สำหรับทดลอง Machine Learning โดยใช้ Docker Compose

## Containers

1. frontend-web
- ใช้ Flask
- ทำหน้าที่แสดงหน้าเว็บ
- รับค่าจากผู้ใช้
- ส่งข้อมูลไปยัง backend API

2. backend-api
- ใช้ FastAPI
- ทำหน้าที่เป็น Machine Learning API
- รับข้อมูลจาก frontend
- ทำนายผลด้วย Linear Regression

## How to Run

```bash
docker compose up --build
