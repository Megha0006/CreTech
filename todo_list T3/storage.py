import json
from task import Task
from todolist import ToDoList

def save_tasks(todo_list, filename="tasks.json"):
    data = [{
        "title": t.title,
        "description": t.description,
        "due_date": t.due_date,
        "completed": t.completed
    } for t in todo_list.tasks]

    with open(filename, "w") as f:
        json.dump(data, f)

def load_tasks(filename="tasks.json"):
    todo_list = ToDoList()
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                task = Task(item["title"], item["description"], item["due_date"])
                if item["completed"]:
                    task.mark_completed()
                todo_list.add_task(task)
    except FileNotFoundError:
        pass
    return todo_list
