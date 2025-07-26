# 🚀 FastAPI Todo API

This is a beginner-friendly Todo API built using **FastAPI** (Python) with a simple frontend test using `fetch()` in **test.html**.

---

## 📁 Project Structure

fastapi-project/
├── main.py # FastAPI backend code (Python)
└── test.html # Simple frontend that calls the API using fetch

yaml
Copy
Edit

---

## 🌐 API Features

- `GET /` — Check if API is working  
- `POST /todos?task=Go to gym` — Add a todo task  
- `GET /todos` — Get the full list of todos  

---

## 🧪 Try Locally

1. **Start the server**

```bash
uvicorn main:app --reload
Open in browser:

http://localhost:8000 – Root check

http://localhost:8000/docs – Swagger UI (API tester)

test.html – Run this file in browser to see fetched todos in console

⚠️ CORS Issue in test.html
You’ll need to enable CORS in main.py if using from another origin (like Live Server):

python
Copy
Edit
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
🧰 Tech Stack
FastAPI (Python)

Uvicorn (ASGI server)

HTML + JavaScript (fetch API)

📦 Run Once with:
bash
Copy
Edit
pip install fastapi uvicorn
👨‍💻 Author
Bissam Iftikhar
GitHub