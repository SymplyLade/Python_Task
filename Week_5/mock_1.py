# To-Do List Application
# List to store tasks
tasks = []
# Function to add

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

# Function to remove
def remove_task():
    if not tasks:
        print("No tasks to remove!")
        return
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
    task_number = int(input("Enter task number to remove: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task number!")
        return
    task = tasks.pop(task_number)
    print(f"Task '{task['task']}' removed successfully!")

# Function to complete task

def complete_task():
    if not tasks:
        print("No tasks to complete!")
        return
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
    task_number = int(input("Enter task number to complete: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("Invalid task number!")
        return
    tasks[task_number]["completed"] = True
    print(f"Task '{tasks[task_number]['task']}' marked as completed!")

# Function to display
def display_tasks():
    if not tasks:
        print("No tasks!")
        return
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
# Function to display all task

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()