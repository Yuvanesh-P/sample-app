# To-Do CLI App

A simple command-line to-do list manager written in Python. No external dependencies required — uses only the standard library.

## Requirements

- Python 3.6 or later

## Usage

Run all commands from the folder containing `todo_app.py`.

### Add a task
```
python todo_app.py add "Buy milk"
```

### List all tasks
```
python todo_app.py list
```

### Mark a task as done
```
python todo_app.py done 1
```

### Remove a task
```
python todo_app.py remove 1
```

> On some systems you may need to use `python3` instead of `python`, depending on how Python is installed.

## How it works

Tasks are stored in a `todos.json` file created automatically in the same folder as `todo_app.py`. Each task has:
- `text` — the task description
- `done` — whether it's completed

## Example session

```
$ python todo_app.py add "Buy milk"
Added: "Buy milk"

$ python todo_app.py add "Walk the dog"
Added: "Walk the dog"

$ python todo_app.py list
[ ] 1. Buy milk
[ ] 2. Walk the dog

$ python todo_app.py done 1
Marked done: Buy milk

$ python todo_app.py list
[x] 1. Buy milk
[ ] 2. Walk the dog

$ python todo_app.py remove 2
Removed: Walk the dog
```
## Git Workflow

This project follows a feature-branch based Git workflow.

### Branches

- `main` - Production/release branch
- `develop` - Development and integration branch
- `feature/login` - Login functionality
- `feature/userprofile` - User profile functionality

### Creating a Feature Branch

Start from the latest `develop` branch:

```bash
git switch develop
git pull origin develop
git switch -c feature/my-feature