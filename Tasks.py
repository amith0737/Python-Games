class Task:
    """Class to represent a Task."""
    def __init__(self, task_id, name, description, status="Pending"):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"ID: {self.task_id}, Name: {self.name}, Description: {self.description}, Status: {self.status}"


class TaskManager:
    """Class to manage CRUD operations for tasks."""
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # Auto-increment ID for tasks

    def create_task(self):
        """Create a new task."""
        name = input("Enter task name: ").strip()
        description = input("Enter task description: ").strip()
        new_task = Task(task_id=self.next_id, name=name, description=description)
        self.tasks.append(new_task)
        print(f"\n✅ Task '{name}' created successfully!")
        self.next_id += 1

    def read_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\n📂 No tasks available.")
        else:
            print("\n📋 List of Tasks:")
            for task in self.tasks:
                print(task)

    def update_task(self):
        """Update an existing task."""
        try:
            task_id = int(input("Enter the Task ID to update: "))
            for task in self.tasks:
                if task.task_id == task_id:
                    task.name = input("Enter new task name: ").strip()
                    task.description = input("Enter new task description: ").strip()
                    task.status = input("Enter new status (Pending/Completed): ").strip().capitalize()
                    print(f"\n✅ Task ID {task_id} updated successfully!")
                    return
            print("\n⚠️ Task not found!")
        except ValueError:
            print("\n⚠️ Invalid input! Please enter a valid Task ID.")

    def delete_task(self):
        """Delete a task."""
        try:
            task_id = int(input("Enter the Task ID to delete: "))
            for task in self.tasks:
                if task.task_id == task_id:
                    self.tasks.remove(task)
                    print(f"\n✅ Task ID {task_id} deleted successfully!")
                    return
            print("\n⚠️ Task not found!")
        except ValueError:
            print("\n⚠️ Invalid input! Please enter a valid Task ID.")


def main():
    """Main function to run the Task Manager application."""
    task_manager = TaskManager()
    print("🛠️ Task Manager Application")
    
    while True:
        print("\nMenu:")
        print("1. Create a Task")
        print("2. View All Tasks")
        print("3. Update a Task")
        print("4. Delete a Task")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task_manager.create_task()
            elif choice == 2:
                task_manager.read_tasks()
            elif choice == 3:
                task_manager.update_task()
            elif choice == 4:
                task_manager.delete_task()
            elif choice == 5:
                print("\n👋 Exiting Task Manager. Goodbye!")
                break
            else:
                print("\n⚠️ Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("\n⚠️ Invalid input! Please enter a number.")

# Run the application
if __name__ == "__main__":
    main()
