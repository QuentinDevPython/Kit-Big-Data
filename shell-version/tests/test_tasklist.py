import datetime
import itertools
import json
import os
from pathlib import Path

import pytest

from src.tasks.task import Task
from src.tasks.tasklist import TaskList


SAMPLE_JSON_FILE = "sample_tasks.json"
TEMP_JSON_FILE = "temp_tasks.json"


@pytest.fixture
def task_list():
    Task.instances = []
    Task.id_task = itertools.count()
    return TaskList()


@pytest.fixture
def sample_tasks():
    sample_tasks = [
        {
            "name": "Sample Task 1",
            "description": "Sample Description 1",
            "due_date": "01/01/2025",
            "completion": 25,
        },
        {
            "name": "Sample Task 2",
            "description": "Sample Description 2",
            "due_date": "02/02/2025",
            "completion": 50,
        },
    ]
    return sample_tasks


@pytest.fixture
def sample_json_file():
    sample_data = {
        "1": {
            "name": "Sample Task 1",
            "description": "Sample Description 1",
            "due_day": 1,
            "due_month": 1,
            "due_year": 2025,
            "completion": 25,
        },
        "2": {
            "name": "Sample Task 2",
            "description": "Sample Description 2",
            "due_day": 2,
            "due_month": 2,
            "due_year": 2025,
            "completion": 50,
        },
    }
    with open(SAMPLE_JSON_FILE, "w") as json_file:
        json.dump(sample_data, json_file)
    yield SAMPLE_JSON_FILE

    os.remove(SAMPLE_JSON_FILE)


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


def test_set_due_date_by_name(task_list):
    task_list.add_task("Task 1", "01/01/2025")
    
    new_due_date = "02/02/2025"
    task_list.set_due_date_by_name("Task 1", new_due_date)

    task = Task.get_task_by_name("Task 1")
    assert task.due_date == datetime.datetime(2025, 2, 2)


def test_set_due_date_by_id(task_list):
    task_list.add_task("Task 1", "01/01/2025")

    new_due_date = "02/02/2025"
    task_list.set_due_date_by_id(1, new_due_date)

    task = Task.get_task_by_id(1)
    assert task.due_date == datetime.datetime(2025, 2, 2)


def test_set_description_by_name(task_list):
    task_list.add_task("Task 1", "01/01/2025", description="Initial description")

    new_description = "Updated description"
    task_list.set_description_by_name("Task 1", new_description)

    task = Task.get_task_by_name("Task 1")
    assert task.description == new_description


def test_set_description_by_id(task_list):
    task_list.add_task("Task 1", "01/01/2025", description="Initial description")

    new_description = "Updated description"
    task_list.set_description_by_id(1, new_description)

    task = Task.get_task_by_id(1)
    assert task.description == new_description


def test_set_task_completion_by_name(task_list):
    task_list.add_task("Task 1", "01/01/2025", completion=25)

    new_completion = 75
    task_list.set_task_completion_by_name("Task 1", new_completion)

    task = Task.get_task_by_name("Task 1")
    assert task.completion == new_completion


def test_set_task_completion_by_id(task_list):
    task_list.add_task("Task 1", "01/01/2025", completion=25)

    new_completion = 75
    task_list.set_task_completion_by_id(1, new_completion)

    task = Task.get_task_by_id(1)
    assert task.completion == new_completion


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


def test_save_tasks(task_list, sample_tasks):
    for task_data in sample_tasks:
        task_list.add_task(
            task_data["name"],
            task_data["due_date"],
            description=task_data["description"],
            completion=task_data["completion"],
        )
    task_list.save_tasks(TEMP_JSON_FILE)

    assert os.path.isfile(TEMP_JSON_FILE)

    with open(TEMP_JSON_FILE, "r") as json_file:
        saved_data = json.load(json_file)

    assert saved_data == {
        "1": {
            "name": "Sample Task 1",
            "description": "Sample Description 1",
            "due_day": 1,
            "due_month": 1,
            "due_year": 2025,
            "completion": 25,
        },
        "2": {
            "name": "Sample Task 2",
            "description": "Sample Description 2",
            "due_day": 2,
            "due_month": 2,
            "due_year": 2025,
            "completion": 50,
        },
    }

    os.remove(TEMP_JSON_FILE)


def test_load_tasks(task_list, sample_json_file):
    task_list.load_tasks(str(sample_json_file))

    assert len(Task.instances) == 2

    task1 = Task.get_task_by_id(1)
    assert task1.name == "Sample Task 1"
    assert task1.description == "Sample Description 1"
    assert task1.due_date == datetime.datetime(2025, 1, 1)
    assert task1.completion == 25

    task2 = Task.get_task_by_id(2)
    assert task2.name == "Sample Task 2"
    assert task2.description == "Sample Description 2"
    assert task2.due_date == datetime.datetime(2025, 2, 2)
    assert task2.completion == 50
