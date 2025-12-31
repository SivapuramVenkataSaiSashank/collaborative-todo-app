# To-Do List Manager - Initial Version
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Exit")
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
