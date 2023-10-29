from task import Task


class TaskList:
    def __init__(self):
        pass

    def add_task(
        self, name: str, due_date: str, description: str = "",
        completion: int = 0
    ):
        Task(name, due_date, description, completion)

    def remove_task_by_name(self, name: str):
        task_to_remove = Task.get_task_by_name(name)
        Task.remove(task_to_remove)

    def remove_task_by_id(self, id: int):
        task_to_remove = Task.get_task_by_id(id)
        Task.remove(task_to_remove)

    def complete_task_by_name(self, name: str):
        Task.get_task_by_name(name).set_completion(100)

    def complete_task_by_id(self, id: int):
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