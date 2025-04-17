import storage

def add_task(task):
    tasks = storage.load_tasks()
    tasks.append(task)
    storage.save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(task):
    tasks = storage.load_tasks()
    if task in tasks:
        tasks.remove(task)
        storage.save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print("Task not found!")

def view_tasks():
    tasks = storage.load_tasks()
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks yet!")
