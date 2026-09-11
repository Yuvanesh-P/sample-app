
#!/usr/bin/env python3
"""
Simple CLI To-Do App with Login

Run:
    python3 todo_app.py login admin admin123
    python3 todo_app.py add "Buy milk"
    python3 todo_app.py list
    python3 todo_app.py done 1
    python3 todo_app.py remove 1
"""

import json
import sys
import os

DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "todos.json"
)

USERNAME = "admin"
PASSWORD = "admin123"


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def login(username, password):
    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False


def add_todo(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f'Added: "{text}"')


def list_todos():
    todos = load_todos()

    if not todos:
        print("No tasks yet. Add one with: python todo_app.py add \"Task\"")
        return

    for i, t in enumerate(todos, start=1):
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {i}. {t['text']}")


def mark_done(index):
    todos = load_todos()

    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"Marked done: {todos[index - 1]['text']}")
    else:
        print("Invalid task number.")


def remove_todo(index):
    todos = load_todos()

    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"Removed: {removed['text']}")
    else:
        print("Invalid task number.")


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python todo_app.py "
            "[login|add|list|done|remove] [args]"
        )
        return

    command = sys.argv[1]

    if command == "login" and len(sys.argv) == 4:
        login(sys.argv[2], sys.argv[3])

    elif command == "add" and len(sys.argv) > 2:
        add_todo(" ".join(sys.argv[2:]))

    elif command == "list":
        list_todos()

    elif command == "done" and len(sys.argv) > 2:
        mark_done(int(sys.argv[2]))

    elif command == "remove" and len(sys.argv) > 2:
        remove_todo(int(sys.argv[2]))

    else:
        print(
            "Usage: python todo_app.py "
            "[login|add|list|done|remove] [args]"
        )


if __name__ == "__main__":
    main()

