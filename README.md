# To-Do System

This Python project provides a simple task management system that allows users to add, edit, delete, and display tasks. Each task has a unique ID, description, priority, and status indicating whether it's completed or not.

## Features

- **Add Tasks**: Add a new task with a specified priority.
- **Edit Tasks**: Modify task details such as description, priority, and completion status.
- **Delete Tasks**: Remove a task from the task list.
- **Display Tasks**: View all tasks or a specific task by ID.
- **Completed Tasks**: Check how many tasks have been completed.

## Class Overview

| Method               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `add_task(task, priority)` | Adds a new task with a description and priority.                        |
| `is_valid(id)`        | Validates if the task with a given ID exists.                               |
| `edit_task(ind, task, priority, is_completed)` | Edits the task details like description, priority, and completion status. |
| `delete_task(ind)`    | Deletes the task at the given index.                                        |
| `completed_tasks()`   | Returns the count of completed tasks.                                       |
| `display_tasks()`     | Displays all tasks.                                                         |
| `display_task(ind)`   | Displays a specific task by its index.                                      |

## Task Object Structure

Each task in the system is represented by a dictionary with the following structure:

```python
{
    "id": int,           # Unique ID of the task
    "task": str,         # Description of the task
    "priority": int,     # Priority level of the task
    "is_complated": bool # Task completion status
}
