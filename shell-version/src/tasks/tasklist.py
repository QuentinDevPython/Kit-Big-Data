"""This module provides a TaskList class to manage a list of tasks."""

from logger import logger
from tasks.task import Task
from utils import read_json, write_json


class TaskList:
    """
    The `TaskList` class manages a list of tasks.

    Example Usage:

    .. code-block:: python

        # Create a new task list
        task_list = TaskList()

        # Add a new task to the list
        task_list.add_task(
            "Task 1", "25/12/2024", "Description for Task 1", completion=0
        )

        # Display all tasks in the list
        task_list.display_tasks()

    """

    def __init__(self):
        """Initialize a new TaskList."""
        pass

    def add_task(
        self, name: str, due_date: str, description: str = "",
        completion: int = 0
    ):
        """
        Add a new task to the task list.

        :param name: The name of the task.
        :type name: str
        :param due_date: The due date of the task (in string format).
        :type due_date: str
        :param description: Additional description of the task
            (default is an empty string).
        :type description: str
        :param completion: The completion status of the task (default is 0).
        :type completion: int
        """
        Task(name, due_date, description, completion)

    def remove_task_by_name(self, name: str):
        """
        Remove a task by its name from the task list.

        :param name: The name of the task to remove.
        :type name: str
        """
        task_to_remove = Task.get_task_by_name(name)
        Task.remove(task_to_remove)

    def remove_task_by_id(self, id: int):
        """
        Remove a task by its unique identifier from the task list.

        :param id: The unique identifier of the task to remove.
        :type id: int
        """
        task_to_remove = Task.get_task_by_id(id)
        Task.remove(task_to_remove)

    def set_due_date_by_name(self, name: str, due_date: str):
        """
        Set the due date of a task by its name.

        :param name: The name of the task.
        :type name: str
        :param due_date: The new due date for the task in string format
            ('DD/MM/YYYY').
        :type due_date: str
        """
        Task.get_task_by_name(name).set_due_date(due_date)

    def set_due_date_by_id(self, id: int, due_date: str):
        """
        Set the due date of a task by its identifier.

        :param id: The unique identifier of the task.
        :type id: int
        :param due_date: The new due date for the task in string format
            ('DD/MM/YYYY').
        :type due_date: str
        """
        Task.get_task_by_id(id).set_due_date(due_date)

    def set_description_by_name(self, name: str, description: str):
        """
        Set the description of a task by its name.

        :param name: The name of the task.
        :type name: str
        :param description: The new description for the task.
        :type description: str
        """
        Task.get_task_by_name(name).set_description(description)

    def set_description_by_id(self, id: int, description: str):
        """
        Set the description of a task by its identifier.

        :param id: The unique identifier of the task.
        :type id: int
        :param description: The new description for the task.
        :type description: str
        """
        Task.get_task_by_id(id).set_description(description)

    def set_task_completion_by_name(self, name: str, completion: int):
        """
        Set the completion status of a task by its name.

        :param name: The name of the task.
        :type name: str
        :param completion: The new completion status for the task (0 to 100).
        :type completion: int
        """
        Task.get_task_by_name(name).set_completion(completion)

    def set_task_completion_by_id(self, id: int, completion: int):
        """
        Set the completion status of a task by its identifier.

        :param id: The unique identifier of the task.
        :type id: int
        :param completion: The new completion status for the task (0 to 100).
        :type completion: int
        """
        Task.get_task_by_id(id).set_completion(completion)

    def complete_task_by_name(self, name: str):
        """
        Mark a task as completed by its name.

        :param name: The name of the task to mark as completed.
        :type name: str
        """
        Task.get_task_by_name(name).set_completion(100)

    def complete_task_by_id(self, id: int):
        """
        Mark a task as completed by its unique identifier.

        :param id: The unique identifier of the task to mark as completed.
        :type id: int
        """
        Task.get_task_by_id(id).set_completion(100)

    def start_of_display(self):
        """Print a header to indicate the start of task display."""
        print()
        print("=====================")
        print("------- TASKS -------")
        print("=====================")
        print()

    def end_of_display(self):
        """Print a footer to indicate the end of task display."""
        print("=====================")
        print("-------- END --------")
        print("=====================")

    def display_tasks(self):
        """Display all tasks in the task list."""
        self.start_of_display()
        for task in Task.get_all_tasks():
            print(task, "\n")
        self.end_of_display()

    def display_tasks_by_completion(self):
        """Display tasks organized by completion status."""
        self.start_of_display()
        print("---- TO DO TASKS ----")
        print()
        for task in Task.get_todo_tasks():
            print(task, "\n")
        print("---- DOING TASKS ----")
        print()
        for task in Task.get_doing_tasks():
            print(task, "\n")
        print("---- DONE TASKS -----")
        print()
        for task in Task.get_done_tasks():
            print(task, "\n")
        self.end_of_display()

    def convert_list_tasks_into_dict(self) -> dict:
        """
        Convert the list of tasks into a dictionary.

        :return: A dictionary representation of the tasks.
        :rtype: dict
        """
        logger.debug("Converting all tasks into dict")
        tasks = {}
        for task in Task.get_all_tasks():
            tasks[task.id] = {
                "name": task.name,
                "description": task.description,
                "due_day": task.due_date.day,
                "due_month": task.due_date.month,
                "due_year": task.due_date.year,
                "completion": task.completion,
            }
        return tasks

    def create_tasks_from_dict(self, tasks: dict):
        """
        Create tasks from a dictionary representation.

        :param tasks: A dictionary containing task data.
        :type tasks: dict
        """
        logger.debug("Creating all tasks from dict")
        for _, task in tasks.items():
            if len(str(task["due_day"])) == 1:
                due_day = f"0{task['due_day']}"
            else:
                due_day = f"{task['due_day']}"

            if len(str(task["due_month"])) == 1:
                due_month = f"0{task['due_month']}"
            else:
                due_month = f"{task['due_month']}"

            due_date = f"{due_day}/{due_month}/{task['due_year']}"
            self.add_task(
                task["name"], due_date, task["description"], task["completion"]
            )

    def save_tasks(self, filepath: str = "src/data/tasks.json"):
        """
        Save the tasks to a JSON file.

        :param filepath: Path to the file to save the data
            (default to data/tasks.json).
        :type filepath: str
        """
        tasks = self.convert_list_tasks_into_dict()
        logger.debug("Saving all tasks into a JSON file")
        write_json(filepath, tasks)

    def load_tasks(self, filepath: str = "src/data/tasks.json"):
        """Load tasks from a JSON file.

        :param filepath: Path to the file to save the data
            (default to data/tasks.json).
        :type filepath: str
        """
        logger.debug("Loading all tasks from a JSON file")
        tasks = read_json(filepath)
        if len(tasks) > 0:
            self.create_tasks_from_dict(tasks)
