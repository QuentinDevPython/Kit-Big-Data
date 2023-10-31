"""This module contains CLI commands for managing tasks."""

import click

from tasks.tasklist import TaskList


task_list = TaskList()


@click.command()
@click.option(
    "--name", prompt="Task name (Required)", type=str, help="Name of the task"
)
@click.option(
    "--due-date",
    prompt="Due date JJ/MM/YYYY (Required)",
    type=str,
    help="Due date of the task",
)
@click.option(
    "--description",
    prompt="Description (Optional)",
    type=str,
    default="",
    help="Description of the task",
)
@click.option(
    "--completion",
    prompt="Completion status 0-100 (Optional)",
    type=int,
    default=0,
    help="Completion status of the task",
)
def add_task(
    name: str, due_date: str, description: str = "", completion: int = 0
):
    """
    Add a new task to the task list.

    :param name: Name of the task.
    :param due_date: Due date of the task (in 'JJ/MM/YYYY' format).
    :param description: Description of the task (optional).
    :param completion: Completion status of the task (optional, 0 to 100).
    """
    task_list.load_tasks()
    task_list.add_task(name, due_date, description, completion)
    task_list.save_tasks()
    print("Task successfully added !")


@click.command("rm-task")
@click.option(
    "--name", prompt="Task name (Required)", type=str,
    help="Name of the task to remove"
)
def remove_task_by_name(name: str):
    """
    Remove a task by its name from the task list.

    :param name: Name of the task to remove.
    """
    task_list.load_tasks()
    task_list.remove_task_by_name(name)
    task_list.save_tasks()
    print("Task successfully removed !")


@click.command("rm-task-id")
@click.option(
    "--id", prompt="Task id (Required)", type=int,
    help="Id of the task to remove"
)
def remove_task_by_id(id: int):
    """
    Remove a task by its unique identifier from the task list.

    :param id: Unique identifier of the task to remove.
    """
    task_list.load_tasks()
    task_list.remove_task_by_id(id)
    task_list.save_tasks()
    print("Task successfully removed !")


@click.command("set-date-task")
@click.option(
    "--name",
    prompt="Task name (Required)",
    type=str,
    help="Name of the task to set due_date",
)
@click.option(
    "--due-date",
    prompt="New due date (Required)",
    type=str,
    help="New due date of the task",
)
def set_due_date_by_name(name: str, due_date: str):
    """
    Set the due date of a task by its name.

    :param name: Name of the task.
    :param due_date: New due date for the task (in 'JJ/MM/YYYY' format).
    """
    task_list.load_tasks()
    task_list.set_due_date_by_name(name, due_date)
    task_list.save_tasks()


@click.command("set-date-task-id")
@click.option(
    "--id",
    prompt="Task id (Required)",
    type=int,
    help="Name of the task to set due_date",
)
@click.option(
    "--due-date",
    prompt="New due date (Required)",
    type=str,
    help="New due date of the task",
)
def set_due_date_by_id(id: int, due_date: str):
    """
    Set the due date of a task by its unique identifier.

    :param id: Unique identifier of the task.
    :param due_date: New due date for the task (in 'JJ/MM/YYYY' format).
    """
    task_list.load_tasks()
    task_list.set_due_date_by_id(id, due_date)
    task_list.save_tasks()


@click.command("set-description-task")
@click.option(
    "--name",
    prompt="Task name (Required)",
    type=str,
    help="Name of the task to set description",
)
@click.option(
    "--description",
    prompt="New description (Required)",
    type=str,
    help="New description of the task",
)
def set_description_by_name(name: str, description: str):
    """
    Set the description of a task by its name.

    :param name: Name of the task.
    :param description: New description for the task.
    """
    task_list.load_tasks()
    task_list.set_description_by_name(name, description)
    task_list.save_tasks()


@click.command("set-description-task-id")
@click.option(
    "--id",
    prompt="Task id (Required)",
    type=int,
    help="Id of the task to set description",
)
@click.option(
    "--description",
    prompt="New description (Required)",
    type=str,
    help="New description of the task",
)
def set_description_by_id(id: int, description: str):
    """
    Set the description of a task by its unique identifier.

    :param id: Unique identifier of the task.
    :param description: New description for the task.
    """
    task_list.load_tasks()
    task_list.set_description_by_id(id, description)
    task_list.save_tasks()


@click.command("set-completion-task")
@click.option(
    "--name",
    prompt="Task name (Required)",
    type=str,
    help="Name of the task to set completion",
)
@click.option(
    "--completion",
    prompt="Completion status (Required)",
    type=int,
    help="Completion status of the task",
)
def set_task_completion_by_name(name: str, completion: int):
    """
    Set the completion status of a task by its name.

    :param name: Name of the task.
    :param completion: New completion status for the task (0 to 100).
    """
    task_list.load_tasks()
    task_list.set_task_completion_by_name(name, completion)
    task_list.save_tasks()


@click.command("set-completion-task-id")
@click.option(
    "--id",
    prompt="Task id (Required)",
    type=int,
    help="Id of the task to set completion",
)
@click.option(
    "--completion",
    prompt="Completion status (Required)",
    type=int,
    help="Completion status of the task",
)
def set_task_completion_by_id(id: int, completion: int):
    """
    Set the completion status of a task by its unique identifier.

    :param id: Unique identifier of the task.
    :param completion: New completion status for the task (0 to 100).
    """
    task_list.load_tasks()
    task_list.set_task_completion_by_id(id, completion)
    task_list.save_tasks()


@click.command("complete-task")
@click.option(
    "--name",
    prompt="Task name (Required)",
    type=str,
    help="Name of the task to complete",
)
def complete_task_by_name(name: str):
    """
    Mark a task as completed by its name.

    :param name: Name of the task to mark as completed.
    """
    task_list.load_tasks()
    task_list.complete_task_by_name(name)
    task_list.save_tasks()
    print("Task successfully completed !")


@click.command("complete-task-id")
@click.option(
    "--id", prompt="Task id (Required)", type=int,
    help="Id of the task to complete"
)
def complete_task_by_id(id: int):
    """
    Mark a task as completed by its unique identifier.

    :param id: Unique identifier of the task to mark as completed.
    """
    task_list.load_tasks()
    task_list.complete_task_by_id(id)
    task_list.save_tasks()
    print("Task successfully completed !")


@click.command("display-tasks")
def display_tasks():
    """Display all tasks in the task list."""
    task_list.load_tasks()
    task_list.display_tasks()
    task_list.save_tasks()


@click.command("display-todo")
def display_tasks_by_completion():
    """Display tasks organized by completion status."""
    task_list.load_tasks()
    task_list.display_tasks_by_completion()
    task_list.save_tasks()
