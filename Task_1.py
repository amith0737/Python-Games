import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except IOError as e:
        print(f"Error saving tasks: {e}")

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task to add: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def task_manager():
    """Main task manager function."""
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    task_manager()
