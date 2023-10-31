"""This module defines the Task class for managing tasks."""

import datetime
import itertools

from src.logger import logger


class Task:
    """
    The `Task` class represents a task.

    Example Usage:

    .. code-block:: python

        # Create a new task
        task = Task(
            "My task", datetime.datetime(2022, 1, 1),
            "This is task 1", 50, "Project A"
        )

        # Set the completion percentage of the task
        task1.set_completion(75)

        # Get all tasks
        all_tasks = Task.get_all_tasks()

    Fields:

    - id_task: A counter to generate unique task IDs.
    - instances: A list to store all task instances.

    """

    id_task = itertools.count()
    instances = []

    def __init__(
        self, name: str, due_date: str, description: str = "",
        completion: int = 0
    ):
        """
        Initialize a Task object.

        :param name: The name of the task.
        :type name: str
        :param due_date: The due date of the task (in the format
            'DD/MM/YYYY').
        :type due_date: str
        :param description: An optional description of the task.
        :type description: str
        :param completion: An optional completion percentage (0 to 100).
        :type completion: int
        """
        self.id = next(Task.id_task) + 1
        self.name = ""
        self.due_date = ""
        self.description = ""
        self.completion = 0

        self.create_task(name, due_date, description, completion)
        Task.instances.append(self)

    def create_task(
        self, name: str, due_date: str, description: str, completion: int
    ):
        """
        Create a task with the specified attributes threw class setters.

        :param name: The name of the task.
        :type name: str
        :param due_date: The due date of the task (in the format
            'DD/MM/YYYY').
        :type due_date: str
        :param description: An optional description of the task.
        :type description: str
        :param completion: An optional completion percentage (0 to 100).
        :type completion: int
        """
        self.set_name(name)
        self.set_due_date(due_date)
        self.set_description(description)
        self.set_completion(completion)

        logger.debug(
            f"Create task : ('Name': {name}, 'Due_date': {due_date},"
            f"'description': {description}, 'completion': {completion}"
        )

    def control_variable_is_string(func):
        """
        Decorate a function to control if a variable is a string.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the variable is not a string.
        """

        def is_string(self, variable):
            if not isinstance(variable, str):
                logger.error(f"{variable} should be of type string")
                raise ValueError(
                    "Le paramètre doit être une chaîne de caractères."
                )
            return func(self, variable)

        return is_string

    def control_variable_is_integer(func):
        """
        Decorate a function to control if a variable is an integer.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the variable is not an integer.
        """

        def is_integer(self, variable):
            if not isinstance(variable, int):
                logger.error(f"{variable} should be of type int")
                raise ValueError("Le paramètre doit être un entier.")
            return func(self, variable)

        return is_integer

    def control_name_validity(func):
        """
        Decorate a function to control the validity of task names.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the name is empty.
        """

        def set_name(self, name: str):
            if not name:
                raise ValueError("Le nom ne peut pas être vide.")
            for task in Task.instances:
                if task.name == name:
                    logger.error(f"{name} should not be an empty string")
                    raise ValueError(
                        "Cette tâche existe déjà. "
                        "Veuillez spécifier un autre nom."
                    )
            return func(self, name)

        return set_name

    @control_variable_is_string
    @control_name_validity
    def set_name(self, name: str):
        """
        Set the name of the task.

        :param name: The new name of the task.
        :type name: str
        """
        logger.debug(f"Setting task name to {name}")
        self.name = name

    def control_date_validity(func):
        """
        Decorate a function to control the validity of due dates.

        This decorator ensures that due dates are in the format
            'DD/MM/YYYY', and they are set to today or a future date.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the date format is incorrect or if the
            date is not today or a future date.
        """

        def set_due_date(self, due_date: str):
            # Control date format
            if not len(due_date.split("/")) == 3:
                raise ValueError("La date doit être de la forme 'JJ/MM/YYYY'")
            day, month, year = due_date.split("/")
            if not len(day) == 2:
                raise ValueError(
                    "Le jour doit être de la forme 'JJ' (deux chiffres)"
                )
            if not len(month) == 2:
                raise ValueError(
                    "Le mois doit être de la forme 'MM' (deux chiffres)"
                )
            if not len(year) == 4:
                raise ValueError(
                    "L'année doit être de la forme 'YYYY' (quatres chiffres)"
                )

            # Control that it's a futur day
            date = datetime.datetime(int(year), int(month), int(day)).date()
            today_date = datetime.datetime.now().date()
            if not date >= today_date:
                logger.error(f"{date} should be a futur day")
                raise ValueError(
                    "La date du jour doit être définie sur la date du jour "
                    f"ou une date future. Date : {due_date}"
                )

            return func(self, due_date)

        return set_due_date

    @control_variable_is_string
    @control_date_validity
    def set_due_date(self, due_date: str):
        """
        Set the due date of the task.

        :param due_date: The new due date of the task.
        :type due_date: datetime
        """
        logger.debug(f"Setting task due_date to {due_date}")
        day, month, year = due_date.split("/")
        self.due_date = datetime.datetime(int(year), int(month), int(day))

    def control_description_validity(func):
        """
        Decorate a function to control the validity of task descriptions.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the description length exceeds 100 characters.
        """

        def set_description(self, description: str):
            if not len(description) <= 100:
                logger.error(
                    f"{description} should have no more than 100 characters"
                )
                raise ValueError(
                    "La description d'une tâche est limitée à 100 caractères"
                )
            return func(self, description)

        return set_description

    @control_variable_is_string
    @control_description_validity
    def set_description(self, description: str):
        """
        Set the description of the task.

        :param description: The new description of the task.
        :type description: str
        """
        logger.debug(f"Setting task description to {description}")
        self.description = description

    def control_completion_validity(func):
        """
        Decorate a function to control the validity of completion percentage.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the completion percentage is not in the
            range [0, 100].
        """

        def set_completion(self, completion: int):
            if (not completion >= 0) or (not completion <= 100):
                logger.error(f"{completion} should be between 0 and 100")
                raise ValueError(
                    "Le taux de complétion doit être compris entre 0 et 100"
                )
            return func(self, completion)

        return set_completion

    @control_variable_is_integer
    @control_completion_validity
    def set_completion(self, completion: int):
        """
        Set the completion percentage of the task.

        :param completion: The new completion percentage of the task.
        :type completion: int
        """
        logger.debug(f"Setting task completion to {completion}")
        self.completion = completion

    @classmethod
    def get_all_tasks(cls):
        """
        Return a list of all the tasks.

        :return: A list of all tasks.
        :rtype: List[Task]
        """
        return cls.instances

    @classmethod
    def get_todo_tasks(cls):
        """
        Get a list of all TODO tasks.

        :return: A list of Task instances with a completion level of 0.
        :rtype: List[Task]
        """
        return list(filter(lambda task: task.completion == 0, cls.instances))

    @classmethod
    def get_doing_tasks(cls):
        """
        Get a list of tasks that are in progress.

        :return: A list of Task instances with a completion level
            between 0 and 100.
        :rtype: List[Task]
        """
        return list(
            filter(
                lambda task: (task.completion > 0) and (task.completion < 100),
                cls.instances,
            )
        )

    @classmethod
    def get_done_tasks(cls):
        """
        Get a list of tasks that are marked as completed.

        :return: A list of Task instances with a completion level of 100.
        :rtype: List[Task]
        """
        return list(filter(lambda task: task.completion == 100, cls.instances))

    @classmethod
    def get_task_by_name(cls, name: str):
        """
        Retrieve a task by its name.

        :param name: The name of the task to retrieve.
        :type name: str
        :return: The task with the specified name.
        :rtype: Task
        :raises IndexError: If no task with the given name is found.
        """
        return list(filter(lambda task: task.name == name, cls.instances))[0]

    @classmethod
    def get_task_by_id(cls, id: int):
        """
        Retrieve a task by its unique identifier.

        :param id: The unique identifier of the task to retrieve.
        :type id: int
        :return: The task with the specified ID.
        :rtype: Task
        :raises IndexError: If no task with the given ID is found.
        """
        return list(filter(lambda task: task.id == id, cls.instances))[0]

    @classmethod
    def remove(cls, task):
        """
        Remove a task from the list of tasks.

        :param task: The task object to remove.
        :type task: Task
        :raises ValueError: If the task is not in the list of tasks.
        """
        logger.debug(
            f"Remove task : ('Name': {task.name},"
            f"'Due_date': {task.due_date},"
            f"'description': {task.description},"
            f"'completion': {task.completion}"
        )
        cls.instances.remove(task)
        del task

    def __repr__(self):
        """
        Return a string representation of the task.

        :return: A string representation of the task.
        :rtype: str
        """
        return (
            f"Tâche {self.id} - {self.name}\n=> A faire pour le "
            f"{self.due_date.day}/{self.due_date.month}/{self.due_date.year}"
            f"\n=> Avancée : {self.completion}%"
        )

    def __str__(self):
        """
        Return a string representation of the task.

        :return: A string representation of the task.
        :rtype: str
        """
        return (
            f"Tâche {self.id} - {self.name}\n=> A faire pour le "
            f"{self.due_date.day}/{self.due_date.month}/{self.due_date.year}"
            f"\n=> Avancée : {self.completion}%"
        )
