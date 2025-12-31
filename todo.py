# To-Do List Manager - Initial Version
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
    print("4. Mark Task as Complete")
    print("5. Exit")

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
            mark_complete(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
