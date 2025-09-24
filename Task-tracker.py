# mini_task_tracker.py

tasks = []

def show_menu():
    print("\n--- Mini Task Tracker ---")
    print("1. Add task")
    print("2. Update task status")
    print("3. View tasks")
    print("4. Exit")

def add_task():
    name = input("Enter task name: ")
    tasks.append({"name": name, "status": "To-do"})
    print(f"Task '{name}' added.")

def update_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            print("Choose new status: [1] To-do [2] In progress [3] Done")
            choice = input("Enter choice: ")
            if choice == "1":
                tasks[idx]["status"] = "To-do"
            elif choice == "2":
                tasks[idx]["status"] = "In progress"
            elif choice == "3":
                tasks[idx]["status"] = "Done"
            print(f"Task '{tasks[idx]['name']}' updated to {tasks[idx]['status']}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\n--- Current Tasks ---")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t['name']} - {t['status']}")

while True:
    show_menu()
    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
