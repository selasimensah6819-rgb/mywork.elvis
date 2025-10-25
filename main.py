import logging

logging.basicConfig(
    filename='app.log',     
    level=logging.INFO,        
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    tasks = []  # store all tasks

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            n_tasks = int(input("\nHow many tasks do you want to add: "))

            for i in range(n_tasks):
                task_name = input(f"Enter task {i+1}: ")
                tasks.append({"task": task_name, "done": False})
                print("Task added!")

        elif choice == '2':
            print('\nTasks:')
            if not tasks:
                print("No tasks added yet.")
            else:
                for index, task in enumerate(tasks):
                    status = 'Done' if task['done'] else 'Not Done'
                    print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as done.")
            else:
                task_index = int(input('Enter the task number to mark as done: ')) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]['done'] = True
                    print('Task marked as done!')
                else:
                    print('Invalid task number.')

        elif choice == '4':
            print('Exiting your To-Do List. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
