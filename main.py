import json
import logging

# ---------------- Setup Logging ----------------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Save/Load Functions ----------------
def load_tasks(filename="tasks.txt"):
    """Load tasks from file if it exists."""
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # If no file or file is empty, return an empty list

def save_tasks(tasks, filename="tasks.txt"):
    """Save tasks to file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# ---------------- Main App ----------------
def main():
    tasks = load_tasks()  # Load tasks when app starts

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            n_tasks = int(input("How many tasks do you want to add? "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                logging.info(f"Added task: {task}")
            save_tasks(tasks)
            print("Task(s) added!")

        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
            logging.info("Displayed tasks")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                save_tasks(tasks)
                print("Task marked as done!")
                logging.info(f"Marked task as done: {tasks[task_index]['task']}")
            else:
                print("Invalid task number.")
                logging.warning("Attempted to mark invalid task number as done")

        elif choice == '4':
            print("Exiting the To-Do List.")
            logging.info("Exited the app.")
            break

        else:
            print("Invalid choice. Please try again.")
            logging.warning("Invalid menu choice entered")


if __name__ == "__main__":
    main()
