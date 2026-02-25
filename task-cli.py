
#!/usr/bin/env python3
"""
Task Tracker CLI - A simple command line tool to manage tasks
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Constants
TASKS_FILE = "tasks.json"
STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in-progress"
STATUS_DONE = "done"


def load_tasks() -> List[Dict]:
    """Load tasks from JSON file. Return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks: List[Dict]) -> None:
    """Save tasks to JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Error saving tasks: {e}", file=sys.stderr)
        sys.exit(1)


def get_next_id(tasks: List[Dict]) -> int:
    """Get the next available task ID."""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1


def add_task(description: str) -> None:
    """Add a new task with 'todo' status."""
    tasks = load_tasks()
    
    new_task = {
        'id': get_next_id(tasks),
        'description': description,
        'status': STATUS_TODO,
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id: int, description: str) -> None:
    """Update an existing task's description."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    
    print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
    sys.exit(1)


def delete_task(task_id: int) -> None:
    """Delete a task by ID."""
    tasks = load_tasks()
    
    original_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    
    if len(tasks) == original_length:
        print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
        sys.exit(1)
    
    save_tasks(tasks)
    print(f"Task deleted successfully (ID: {task_id})")


def mark_task_status(task_id: int, status: str) -> None:
    """Mark a task with a specific status."""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status} (ID: {task_id})")
            return
    
    print(f"Error: Task with ID {task_id} not found", file=sys.stderr)
    sys.exit(1)


def list_tasks(status: Optional[str] = None) -> None:
    """List all tasks or filter by status."""
    tasks = load_tasks()
    
    if status:
        # Validate status
        valid_statuses = [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]
        if status not in valid_statuses:
            print(f"Error: Invalid status '{status}'. Valid statuses are: {', '.join(valid_statuses)}", file=sys.stderr)
            sys.exit(1)
        
        filtered_tasks = [task for task in tasks if task['status'] == status]
        print(f"\
Tasks with status '{status}':")
    else:
        filtered_tasks = tasks
        print("\
All Tasks:")
    
    if not filtered_tasks:
        print("No tasks found.")
        return
    
    # Sort by ID for consistent display
    filtered_tasks.sort(key=lambda x: x['id'])
    
    for task in filtered_tasks:
        print(f"\
ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['createdAt']}")
        print(f"Updated: {task['updatedAt']}")


def print_usage() -> None:
    """Print usage instructions."""
    print("Task Tracker CLI - Usage:")
    print("\
Add a new task:")
    print("  task-cli add \"Task description\"")
    print("\
Update a task:")
    print("  task-cli update <id> \"New description\"")
    print("\
Delete a task:")
    print("  task-cli delete <id>")
    print("\
Mark task as in-progress:")
    print("  task-cli mark-in-progress <id>")
    print("\
Mark task as done:")
    print("  task-cli mark-done <id>")
    print("\
List all tasks:")
    print("  task-cli list")
    print("\
List tasks by status:")
    print("  task-cli list todo")
    print("  task-cli list in-progress")
    print("  task-cli list done")


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Please provide a task description", file=sys.stderr)
                sys.exit(1)
            description = " ".join(sys.argv[2:])
            add_task(description)
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Please provide task ID and new description", file=sys.stderr)
                sys.exit(1)
            task_id = int(sys.argv[2])
            description = " ".join(sys.argv[3:])
            update_task(task_id, description)
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID", file=sys.stderr)
                sys.exit(1)
            task_id = int(sys.argv[2])
            delete_task(task_id)
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID", file=sys.stderr)
                sys.exit(1)
            task_id = int(sys.argv[2])
            mark_task_status(task_id, STATUS_IN_PROGRESS)
        
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID", file=sys.stderr)
                sys.exit(1)
            task_id = int(sys.argv[2])
            mark_task_status(task_id, STATUS_DONE)
        
        elif command == "list":
            if len(sys.argv) >= 3:
                status = sys.argv[2].lower()
                list_tasks(status)
            else:
                list_tasks()
        
        else:
            print(f"Error: Unknown command '{command}'", file=sys.stderr)
            print_usage()
            sys.exit(1)
    
    except ValueError:
        print("Error: Invalid task ID. Please provide a valid number.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

