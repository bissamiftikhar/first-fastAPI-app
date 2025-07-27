from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "API is dockerized working!"}

# Todo list storage
todos = []

@app.post("/todos")
def add_todo(task: str):
    todos.append(task)
    return {"message": "Todo ci.cd ya Allah  .. ,done ia, IA no rahh docker hsameetadded!"}

@app.get("/todos")
def get_todos():
    return {"todos": todos}
