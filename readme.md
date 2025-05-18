# 📬 Notification Service

A FastAPI-based notification service that supports Email, SMS, and In-App notifications using RabbitMQ and MongoDB.

---

## 🚀 Features

- REST API to send and retrieve notifications
- Supports notification types: `email`, `sms`, and `in-app`
- RabbitMQ-based queuing for async processing
- Retry mechanism for failed notifications
- MongoDB for persistence


---

## 🧰 Tech Stack

- FastAPI
- RabbitMQ (via aio-pika)
- MongoDB (via Motor)
- Tenacity for retries

---

## 🛠️ Setup Instructions

###

```bash
git clone https://github.com/Anushaamar111/Pepsales-AI.git
cd notification-service
python -m venv venv
On Windows: venv\Scripts\activate
RabbitMQ- docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 rabbitmq
uvicorn main:app --reload
python app/worker.py


