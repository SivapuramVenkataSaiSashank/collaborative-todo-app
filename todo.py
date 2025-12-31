# To-Do List Manager - Initial Version
<<<<<<< HEAD
def mark_complete(tasks):
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)
    index = int(input("Enter task number to mark complete: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index] = tasks[index] + " ✔"
        print("Task marked as complete.")
    else:
        print("Invalid task number.")
=======
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

<<<<<<< HEAD
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid task number.")
=======
def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Exit")
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")
>>>>>>> 85e47026e881ada5dfe24673c603e8e064c64ff9
>>>>>>> 9e0514fef5ef2c0d9d23e2adb7ad55e79a0d9ebf

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
<<<<<<< HEAD
    print("4. Mark Task as Complete")
    print("5. Exit")
=======
    print("4. Exit")
>>>>>>> 9e0514fef5ef2c0d9d23e2adb7ad55e79a0d9ebf

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
<<<<<<< HEAD
            mark_complete(tasks)
        elif choice == "5":
=======
            print("Exiting application.")
>>>>>>> 9e0514fef5ef2c0d9d23e2adb7ad55e79a0d9ebf
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
