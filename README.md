# 🚀 FastAPI Todo API

A simple REST API for managing todo tasks using **FastAPI**, along with a minimal HTML frontend using the `fetch` API for testing.

---

## 📁 Project Structure

fastapi-project/
├── main.py # FastAPI backend code
└── test.html # Frontend to fetch todos from API

yaml
Copy
Edit

---

## 🔧 Features

- ✅ `GET /` – Check if API is working
- ✅ `POST /todos?task=Go to gym` – Add a new todo task
- ✅ `GET /todos` – Retrieve all todos

---

## ▶️ Running the Project Locally

### 1. Install dependencies

```bash
pip install fastapi uvicorn
2. Run the FastAPI server
bash
Copy
Edit
uvicorn main:app --reload
3. Access in your browser
API root: http://localhost:8000

Swagger UI: http://localhost:8000/docs

Todos API: http://localhost:8000/todos

🌐 Frontend Testing
Open test.html in a browser. It uses JavaScript's fetch() to call the /todos endpoint and logs the data to the console.

test.html Example:
html
Copy
Edit
<script>
  fetch("http://localhost:8000/todos")
    .then(res => res.json())
    .then(data => console.log(data));
</script>
Open DevTools → Console to view the todos.

🛡️ Fixing CORS Error (if needed)
If you're accessing the API from a different origin (like Live Server), add this middleware to main.py:

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
⚙️ Tech Stack
FastAPI – Python web framework

Uvicorn – ASGI server

HTML + JavaScript – Frontend for testing

🧑‍💻 Author
Bissam Iftikhar
GitHub: @bissamiftikhar

📌 License
This project is for learning/demo purposes and doesn't use a specific license.