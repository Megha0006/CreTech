from task import Task
from todolist import ToDoList
from storage import save_tasks, load_tasks

if __name__ == "__main__":
    todo = load_tasks()

    # Sample tasks
    t1 = Task("Buy groceries", "Milk, eggs, and bread", "2025-05-23")
    t2 = Task("Study Python", "Complete file handling section", "2025-05-25")

    todo.add_task(t1)
    todo.add_task(t2)

    todo.mark_task_completed("Buy groceries")
    todo.remove_task("Study Python")

    todo.show_tasks()

    save_tasks(todo)
