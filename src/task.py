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
        self.name = name
        self.due_date = due_date
        self.description = description
        self.completion = completion
        Task.instances.append(self)

    def set_name(self, name: str):
        """
        Sets the name of the task.

        :param name: The new name of the task.
        :type name: str
        """
        self.name = name

    def set_due_date(self, due_date: str):
        """
        Sets the due date of the task.

        :param due_date: The new due date of the task.
        :type due_date: datetime
        """
        day, month, year = due_date.split("/")
        self.due_date = datetime.datetime(int(year), int(month), int(day))

    def set_description(self, description: str):
        """
        Sets the description of the task.

        :param description: The new description of the task.
        :type description: str
        """
        self.description = description

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
