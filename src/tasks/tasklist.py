from task import Task
from utils import read_json, write_json

class TaskList:
    def __init__(self):
        pass

    def add_task(
        self, name: str, due_date: str, description: str = "", completion: int = 0
    ):
        """
        Add a new task to the task list.

        :param name: The name of the task.
        :type name: str

        :param due_date: The due date of the task (in string format).
        :type due_date: str

        :param description: Additional description of the task (default is an empty string).
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
        Task.get_task_by_name(name).set_due_date(due_date)

    def set_due_date_by_id(self, id: int, due_date: str):
        Task.get_task_by_id(id).set_due_date(due_date)

    def set_description_by_name(self, name: str, description: str):
        Task.get_task_by_name(name).set_description(description)

    def set_description_by_id(self, id: int, description: str):
        Task.get_task_by_id(id).set_description(description)

    def set_task_completion_by_name(self, name: str, completion: int):
        Task.get_task_by_name(name).set_completion(completion)

    def set_task_completion_by_id(self, id: int, completion: int):
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
        print()
        print("=====================")
        print("------- TASKS -------")
        print("=====================")
        print()

    def end_of_display(self):
        print("=====================")
        print("-------- END --------")
        print("=====================")

    def display_tasks(self):
        self.start_of_display()
        for task in Task.get_all_tasks():
            print(task, "\n")
        self.end_of_display()

    def display_tasks_by_completion(self):
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

    def save_tasks(self):
        tasks = self.convert_list_tasks_into_dict()
        write_json("../data/tasks.json", tasks)

    def load_tasks(self):
        tasks = read_json("../data/tasks.json")
        self.create_tasks_from_dict(tasks)
