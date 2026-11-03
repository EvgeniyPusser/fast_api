from fastapi import FastAPI

from itertools import count

from fastapi import HTTPException

from models.task_models import TaskDTO, Task

app = FastAPI()

tasks_db = []
task_ids = count()


@app.post("/tasks")
def create_task(task_dto: TaskDTO):
    task = Task(title=task_dto.title, description=task_dto.description,
                id=next(task_ids))
    tasks_db.append(task)
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return tasks_db[skip:skip+limit]


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_dto: TaskDTO):
    task = get_task(task_id)
    task.title = task_dto.title
    task.description = task_dto.description
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = get_task(task_id)
    tasks_db.remove(task)
    return task


@app.get("/health")
async def health():
    return {"status": "ok"}
