# To-Do List Manager - Initial Version

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Exit")

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
