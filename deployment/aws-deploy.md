# 🛰️ FastAPI Deployment to AWS EC2

This document logs how the FastAPI Todo API was deployed to an AWS EC2 instance.

---

## ✅ Setup Summary

| Step | Task |
|------|------|
| 1️⃣ | Launched EC2 instance (Ubuntu 22.04) |
| 2️⃣ | Opened ports 22 (SSH) and 8000 (API) in the security group |
| 3️⃣ | Connected via SSH |
| 4️⃣ | Installed Python3, pip, and created a virtual environment |
| 5️⃣ | Cloned the GitHub repo |
| 6️⃣ | Installed FastAPI & Uvicorn inside virtualenv |
| 7️⃣ | Ran app using `uvicorn main:app --host 0.0.0.0 --port 8000` |

---

## 🌐 Accessing the API

- Public IPv4: `http://56.228.34.122:8000`
- Example endpoint: `http://56.228.34.122:8000/todos`
- API Docs: `http://56.228.34.122:8000/docs`

---
## 🖼️ Screenshots

### EC2 Instance
![EC2](../assets/fastapi-todo-2.png)

### /todos Endpoint in Browser
![Todos](../assets/fastapi-todo-1.png)

---

## ⚠️ Common Issues & Fixes

### 🔒 Port 80 Permission Error

When running on port 80:

