# 📝 FastAPI Todo API

A simple REST API built with **FastAPI** and a minimal **HTML frontend**.

---

## 📁 Project Structure

- `main.py` – FastAPI backend with `/todos` endpoint  
- `test.html` – HTML file using `fetch()` to get todos  
- `deployment/aws-deploy.md` – AWS EC2 deployment steps  

---

## 🚀 Deployment

📄 [EC2 Setup Guide →](deployment/aws-deploy.md)

---

## ⚙️ Run Locally

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install packages
pip install fastapi uvicorn

# 3. Start API server
uvicorn main:app --reload
```

Visit:
- 🧪 API: [http://localhost:8000/todos](http://localhost:8000/todos)  
- 📘 Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Frontend Demo (`test.html`)

```html
<script>
fetch("http://localhost:8000/todos")
  .then(res => res.json())
  .then(data => console.log(data));
</script>
```

Open in browser → Inspect → Console → View response.

---

## 🛠 Built With

- Python + FastAPI
- Uvicorn
- HTML + JS

---

## 👤 Author

[Bissam Iftikhar](https://github.com/bissamiftikhar)