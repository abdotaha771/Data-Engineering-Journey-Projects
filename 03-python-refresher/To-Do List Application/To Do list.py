import json
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []
    except Exception as exc:
        print(f"Error loading tasks: {exc}")
        return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as exc:
        print(f"Error saving tasks to file: {exc}")


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    tasks.append({"title": task, "done": False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list yet.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task.get("done") else "✗"
        title = task.get("title", "Untitled task")
        print(f"{index}. [{status}] {title}")
    print()


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to mark as done: ").strip())
    except ValueError:
        print("Please enter a valid task number.")
        return

    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        task["done"] = True
        save_tasks(tasks)
        print(f"Task '{task.get('title', 'Unknown task')}' marked as done.")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to delete: ").strip())
    except ValueError:
        print("Please enter a valid task number.")
        return

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task.get('title', 'Unknown task')}' deleted successfully.")
    else:
        print("Invalid task number.")


def show_menu():
    print("\n========= TO-DO LIST =========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("==============================")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        try:
            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                mark_task_done(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 5.")
        except KeyboardInterrupt:
            print("\nExiting the to-do list. Goodbye!")
            break
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")


if __name__ == "__main__":
    main()


