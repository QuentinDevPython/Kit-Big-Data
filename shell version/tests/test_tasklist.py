import itertools
import pytest

from src.tasks.task import Task
from src.tasks.tasklist import TaskList


@pytest.fixture
def task_list():
    Task.instances = []
    Task.id_task = itertools.count()
    return TaskList()


def test_add_task(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    assert len(Task.instances) == 1


def test_remove_task_by_name(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    task_list.remove_task_by_name("Task 1")
    assert len(Task.instances) == 0


def test_remove_task_by_id(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    task_list.remove_task_by_id(1)
    assert len(Task.instances) == 0


def test_complete_task_by_name(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    task_list.complete_task_by_name("Task 1")
    assert Task.instances[0].completion == 100


def test_complete_task_by_id(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    task_list.complete_task_by_id(1)
    assert Task.instances[0].completion == 100


def test_display_tasks(capsys, task_list):
    task_list.add_task("Task 1", "01/01/2025")
    task_list.add_task("Task 2", "01/01/2025")

    task_list.display_tasks()

    captured = capsys.readouterr()
    expected_output = (
        "\n"
        "=====================\n"
        "------- TASKS -------\n"
        "=====================\n"
        "\n"
        "Tâche 1 - Task 1\n=> A faire pour le 1/1/2025\n=> Avancée : 0% \n\n"
        "Tâche 2 - Task 2\n=> A faire pour le 1/1/2025\n=> Avancée : 0% \n\n"
        "=====================\n"
        "-------- END --------\n"
        "=====================\n"
    )
    assert captured.out == expected_output


def test_display_tasks_by_completion(capsys, task_list):
    task_list.add_task("Task 1", "01/01/2025", completion=20)
    task_list.add_task("Task 2", "01/01/2025")
    task_list.add_task("Task 3", "01/01/2025", completion=100)

    task_list.display_tasks_by_completion()

    captured = capsys.readouterr()
    expected_output = (
        "\n"
        "=====================\n"
        "------- TASKS -------\n"
        "=====================\n"
        "\n"
        "---- TO DO TASKS ----\n"
        "\n"
        "Tâche 2 - Task 2\n=> A faire pour le 1/1/2025\n=> Avancée : 0% \n\n"
        "---- DOING TASKS ----\n"
        "\n"
        "Tâche 1 - Task 1\n=> A faire pour le 1/1/2025\n=> Avancée : 20% \n\n"
        "---- DONE TASKS -----\n"
        "\n"
        "Tâche 3 - Task 3\n=> A faire pour le 1/1/2025\n=> Avancée : 100% \n\n"
        "=====================\n"
        "-------- END --------\n"
        "=====================\n"
    )
    assert captured.out == expected_output


def test_convert_list_tasks_into_dict(task_list):
    task_list.add_task("Task 1", "01/01/2025", completion=20)
    task_dict = task_list.convert_list_tasks_into_dict()
    expected_task_dict = {
        1: {
            "name": "Task 1",
            "description": "",
            "due_day": 1,
            "due_month": 1,
            "due_year": 2025,
            "completion": 20,
        }
    }
    assert task_dict == expected_task_dict


def test_create_tasks_from_dict(task_list):
    task_dict = {
        1: {
            "name": "Task 1",
            "description": "",
            "due_day": 1,
            "due_month": 1,
            "due_year": 2025,
            "completion": 20,
        },
        2: {
            "name": "Task 2",
            "description": "",
            "due_day": 11,
            "due_month": 11,
            "due_year": 2025,
            "completion": 20,
        },
    }
    task_list.create_tasks_from_dict(task_dict)

    assert len(Task.instances) == 2
