# Task Tracker CLI

A simple command line interface (CLI) tool to track and manage your tasks efficiently. This application allows you to add, update, delete, and organize tasks with different statuses, all stored in a JSON file.

https://roadmap.sh/projects/task-tracker

## Features

- ✅ Add Tasks: Create new tasks with descriptions

- ✏️ Update Tasks: Modify existing task descriptions

- 🗑️ Delete Tasks: Remove tasks you no longer need

- 📋 List Tasks: View all tasks or filter by status

- 🔄 Status Management: Mark tasks as todo, in-progress, or done

- 💾 Persistent Storage: All tasks are saved in a JSON file

- 🛡️ Error Handling: Graceful handling of invalid inputs and edge cases

## Requirements

- Python 3.6 or higher

- No external dependencies required (uses only Python standard library)

## Installation

- Clone or download this repository

- Navigate to the project directory

- Make the script executable (optional, on Unix-like systems):

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

chmod +x task-cli.py

## Usage

### Basic Command Structure

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py `<command>` `[arguments]`

Or if you've made it executable:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

./task-cli.py `<command>` `[arguments]`

### Available Commands

#### 1. Add a New Task

Add a new task to your task list:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py add "Buy groceries"

Output:

Task added successfully (ID: 1)

#### 2. Update a Task

Update the description of an existing task:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py update 1 "Buy groceries and cook dinner"

Output:

Task updated successfully (ID: 1)

#### 3. Delete a Task

Remove a task from your task list:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py delete 1

Output:

Task deleted successfully (ID: 1)

#### 4. Mark Task as In Progress

Change a task's status to "in-progress":

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py mark-in-progress 1

Output:

Task marked as in-progress (ID: 1)

#### 5. Mark Task as Done

Change a task's status to "done":

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py mark-done 1

Output:

Task marked as done (ID: 1)

#### 6. List All Tasks

Display all tasks in your task list:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py list

Output:

All Tasks:

ID: 1
Description: Buy groceries and cook dinner
Status: in-progress
Created: 2024-01-15T10:30:00.123456
Updated: 2024-01-15T11:00:00.789012

ID: 2
Description: Complete project documentation
Status: done
Created: 2024-01-15T09:00:00.456789
Updated: 2024-01-15T12:00:00.345678

#### 7. List Tasks by Status

Filter and display tasks based on their status:

List todo tasks:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py list todo

List in-progress tasks:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py list in-progress

List done tasks:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py list done

Output:

Tasks with status 'done':

ID: 2
Description: Complete project documentation
Status: done
Created: 2024-01-15T09:00:00.456789
Updated: 2024-01-15T12:00:00.345678

## Task Properties

Each task in the system has the following properties:

- id: A unique identifier for the task (auto-incremented)

- description: A short description of the task

- status: The current status of the task (todo, in-progress, or done)

- createdAt: The date and time when the task was created (ISO 8601 format)

- updatedAt: The date and time when the task was last updated (ISO 8601 format)

Data Storage

All tasks are stored in a tasks.json file in the same directory as the script. The file is automatically created when you add your first task. The JSON structure is as follows:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

[

  {

    "id": 1,

    "description": "Buy groceries and cook dinner",

    "status": "in-progress",

    "createdAt": "2024-01-15T10:30:00.123456",

    "updatedAt": "2024-01-15T11:00:00.789012"

  },

  {

    "id": 2,

    "description": "Complete project documentation",

    "status": "done",

    "createdAt": "2024-01-15T09:00:00.456789",

    "updatedAt": "2024-01-15T12:00:00.345678"

  }

]

## Error Handling

The application includes comprehensive error handling for various scenarios:

-

Invalid Task ID: If you provide a non-existent task ID, you'll receive an error message

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py delete 999

Output: Error: Task with ID 999 not found

-

Invalid Task ID Format: If you provide a non-numeric task ID

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py update abc "test"

`Output: Error: Invalid task ID. Please provide a valid number`

-

Invalid Status: If you provide an invalid status when listing tasks

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py list invalid

`Output: Error: Invalid status 'invalid'. Valid statuses are: todo, in-progress, done`

-

Missing Arguments: If you don't provide required arguments, usage instructions are displayed

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py add

`Output: Error: Please provide a task description`

-

Unknown Commands: If you provide an invalid command, usage instructions are displayed

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

python3 task-cli.py unknown-command

`Output: Error: Unknown command 'unknown-command'`

## Examples

### Example Workflow

Here's a complete example workflow showing how to use the Task Tracker CLI:

[data-radix-scroll-area-viewport]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}[data-radix-scroll-area-viewport]::-webkit-scrollbar{display:none}

## Technical Details

- Language: Python 3

- Dependencies: None (uses only Python standard library)

- Data Format: JSON

- File System: Uses Python's built-in json and os modules

- Date/Time: Uses Python's datetime module for timestamps

## Project Structure

task-tracker-cli/
├── task-cli.py      # Main application script
├── tasks.json       # Data storage file (auto-created)
├── README.md        # This file
└── todo.md          # Development task tracking

## Development

This project was developed as a practice exercise to demonstrate:

- Command line interface development

- File system operations

- JSON data handling

- Error handling and validation

- User input processing

- Data persistence

## Future Enhancements

Potential improvements for future versions:

- Task priority levels

- Due dates and reminders

- Task categories/tags

- Search functionality

- Export tasks to different formats

- Interactive mode

- Task dependencies

- Subtasks support

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. Suggestions and feedback are welcome!

## Author

Created as a learning project to practice CLI development and task management concept.

