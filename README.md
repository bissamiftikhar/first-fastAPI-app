# 📝 FastAPI Todo API

A simple Todo API built using **FastAPI** and a minimal **HTML frontend** to fetch todos.

---

## 📂 Files

- `main.py` – FastAPI backend with todo endpoints
- `test.html` – Frontend file using `fetch()` to access the API

---

## ⚙️ How to Run Locally

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install required packages

```bash
pip install fastapi uvicorn
```

### 3. Run the API server

```bash
uvicorn main:app --reload
```

### 4. Open in browser

- ✅ Root check: [http://localhost:8000](http://localhost:8000)
- ✅ API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ✅ Todos: [http://localhost:8000/todos](http://localhost:8000/todos)

---

## 💡 Example Usage

- Add todo: `POST /todos?task=Go to gym`
- Get all todos: `GET /todos`

---

## 🌐 Frontend (test.html)

```html
<script>
  fetch("http://localhost:8000/todos")
    .then(res => res.json())
    .then(data => console.log(data));
</script>
```

Open this file in your browser → Right-click → Inspect → Console → See the todo list.

---

## 🧠 Notes

- You may get **CORS** error if using Live Server. Fix it by adding CORS middleware in `main.py`.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🛠 Built With

- Python
- FastAPI
- Uvicorn
- HTML + JavaScript

---

## 👨‍💻 Author

[Bissam Iftikhar](https://github.com/bissamiftikhar)