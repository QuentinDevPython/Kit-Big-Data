import datetime
import itertools


class Task:
    id_task = itertools.count()
    instances = []

    def __init__(
        self, name: str, due_date: str, description: str = "",
        completion: int = 0
    ):
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
        self.set_name(name)
        self.set_due_date(due_date)
        self.set_description(description)
        self.set_completion(completion)

    def control_variable_is_string(func):
        """
        Decorator function for controlling if a variable is a string.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the variable is not a string.
        """

        def is_string(self, variable):
            if not isinstance(variable, str):
                raise ValueError(
                    "Le paramètre doit être une chaîne de caractères."
                )
            return func(self, variable)

        return is_string

    def control_variable_is_integer(func):
        """
        Decorator function for controlling if a variable is an integer.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the variable is not an integer.
        """

        def is_integer(self, variable):
            if not isinstance(variable, int):
                raise ValueError("Le paramètre doit être un entier.")
            return func(self, variable)

        return is_integer

    def control_name_validity(func):
        """
        Decorator function for controlling the validity of task names.

        This decorator ensures that task names are not empty.

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
        Sets the name of the task.

        :param name: The new name of the task.
        :type name: str
        """
        self.name = name

    def control_date_validity(func):
        """
        Decorator function for controlling the validity of due dates.

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
            # Contrôler le format de la date
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

            # Contrôler que la date est le jour d'aujourd'hui (ou ultérieur)
            date = datetime.datetime(int(year), int(month), int(day)).date()
            today_date = datetime.datetime.now().date()
            if not date >= today_date:
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
        Sets the due date of the task.

        :param due_date: The new due date of the task.
        :type due_date: datetime
        """
        day, month, year = due_date.split("/")
        self.due_date = datetime.datetime(int(year), int(month), int(day))

    def control_description_validity(func):
        """
        Decorator function for controlling the validity of task descriptions.

        This decorator ensures that task descriptions do not exceed 100 
        characters in length.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the description length exceeds 100 characters.
        """

        def set_description(self, description: str):
            if not len(description) <= 100:
                raise ValueError(
                    "La description d'une tâche est limitée à 100 caractères"
                )
            return func(self, description)

        return set_description

    @control_variable_is_string
    @control_description_validity
    def set_description(self, description: str):
        """
        Sets the description of the task.

        :param description: The new description of the task.
        :type description: str
        """
        self.description = description

    def control_completion_validity(func):
        """
        Decorator function to control the validity of completion percentage.

        This decorator ensures that the completion percentage falls within 
        the range of 0 to 100%.

        :param func: The function to be decorated.
        :type func: callable
        :return: The decorated function.
        :rtype: callable
        :raises ValueError: If the completion percentage is not in the 
            range [0, 100].
        """

        def set_completion(self, completion: int):
            if (not completion >= 0) or (not completion <= 100):
                raise ValueError(
                    "Le taux de complétion doit être compris entre 0 et 100"
                )
            return func(self, completion)

        return set_completion

    @control_variable_is_integer
    @control_completion_validity
    def set_completion(self, completion: int):
        """
        Sets the completion percentage of the task.

        :param completion: The new completion percentage of the task.
        :type completion: int
        """
        self.completion = completion

    @classmethod
    def get_all_tasks(cls):
        """
        Returns a list of all the tasks.

        :return: A list of all tasks.
        :rtype: List[Task]
        """
        return cls.instances

    @classmethod
    def get_todo_tasks(cls):
        """
        Get a list of all TODO tasks within the class's instances.

        :return: A list of Task instances with a completion level of 0.
        :rtype: List[Task]
        """
        return list(filter(lambda task: task.completion == 0, cls.instances))

    @classmethod
    def get_doing_tasks(cls):
        return list(
            filter(
                lambda task: (task.completion > 0) and (task.completion < 100),
                cls.instances,
            )
        )

    @classmethod
    def get_done_tasks(cls):
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
        cls.instances.remove(task)
        del task

    def __repr__(self):
        """
        Returns a string representation of the task.

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
        Returns a string representation of the task.

        :return: A string representation of the task.
        :rtype: str
        """
        return (
            f"Tâche {self.id} - {self.name}\n=> A faire pour le "
            f"{self.due_date.day}/{self.due_date.month}/{self.due_date.year}"
            f"\n=> Avancée : {self.completion}%"
        )
