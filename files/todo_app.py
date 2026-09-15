import json
import os
import sys

TODO_FILE = "todos.json"


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []

    with open(TODO_FILE, "r") as file:
        return json.load(file)


def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        json.dump(todos, file, indent=4)


# ---------------- LOGIN ----------------

def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False


# ---------------- USER PROFILE ----------------

def show_profile():
    print("User Profile")
    print("Username: admin")
    print("Role: Standard User")
    print("Status: Active")


# ---------------- TODO FUNCTIONS ----------------

def get_task_text(todo):
    """Support both old 'text' and new 'task' todo formats."""
    return todo.get("task", todo.get("text", ""))


def add_todo(task):
    todos = load_todos()

    todos.append({
        "task": task,
        "done": False
    })

    save_todos(todos)
    print("Todo added successfully.")


def list_todos():
    todos = load_todos()

    if not todos:
        print("No todos found.")
        return

    for index, todo in enumerate(todos, start=1):
        task = get_task_text(todo)
        status = "Done" if todo.get("done", False) else "Pending"
        print(f"{index}. {task} - {status}")


def done_todo(task_id):
    todos = load_todos()

    if task_id < 1 or task_id > len(todos):
        print("Error: Invalid task number.")
        return

    todos[task_id - 1]["done"] = True
    save_todos(todos)

    print("Todo marked as done.")


def remove_todo(task_id):
    todos = load_todos()

    if task_id < 1 or task_id > len(todos):
        print("Error: Invalid task number.")
        return

    removed_task = todos.pop(task_id - 1)
    task = get_task_text(removed_task)

    save_todos(todos)

    print(f"Todo removed: {task}")


# ---------------- MAIN ----------------

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python todo_app.py login <username> <password>")
        print("  python todo_app.py profile")
        print("  python todo_app.py add <task>")
        print("  python todo_app.py list")
        print("  python todo_app.py done <task_number>")
        print("  python todo_app.py remove <task_number>")
        return

    command = sys.argv[1]

    if command == "login":
        if len(sys.argv) != 4:
            print("Usage: python todo_app.py login <username> <password>")
            return

        username = sys.argv[2]
        password = sys.argv[3]

        login(username, password)

    elif command == "profile":
        show_profile()

    elif command == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo_app.py add <task>")
            return

        task = " ".join(sys.argv[2:])
        add_todo(task)

    elif command == "list":
        list_todos()

    elif command == "done":
        if len(sys.argv) != 3:
            print("Usage: python todo_app.py done <task_number>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task number must be a number.")
            return

        done_todo(task_id)

    elif command == "remove":
        if len(sys.argv) != 3:
            print("Usage: python todo_app.py remove <task_number>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task number must be a number.")
            return

        remove_todo(task_id)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()