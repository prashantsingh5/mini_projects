tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added: ", task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed: ", task)
    else:
        print("Task not found!")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    while True:
        print("\n---- To-Do List Application ----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()
