import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def removed_task(self, task):
        if task in self.tasks:
            self.tasks.removed(task)
            print(f"Task '{task}' view.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("Your To-Do list is empty!")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")
        print("Tasks saved to tasks.txt.")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            print("Tasks loaded from tasks.txt.")
        else:
            print("No saved tasks found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Removed Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.save_tasks()
        elif choice == '5':
            todo_list.load_tasks()
        elif choice == '6':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()