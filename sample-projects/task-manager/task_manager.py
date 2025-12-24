import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, "r") as f:
        return json.load(f)   # BUG: crashes if file is empty/corrupt


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)   # BUG: no formatting, no error handling


def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1  # BUG: breaks if tasks deleted
    tasks[task_id] = {
        "title": title,
        "completed": False
    }
    save_tasks(tasks)


def complete_task(task_id):
    tasks = load_tasks()
    tasks[str(task_id)]["completed"] = True  # BUG: key mismatch (int vs str)
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    for tid, task in tasks.items():
        status = "✓" if task["completed"] else "✗"
        print(f"{tid}. {task['title']} [{status}]")


def main():
    while True:
        print("\n1. Add task")
        print("2. Complete task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            task_id = input("Task ID: ")
            complete_task(task_id)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
