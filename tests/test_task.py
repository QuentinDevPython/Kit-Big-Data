import datetime
import pytest

from src.tasks.task import Task


def test_control_name_validity_empty():
    with pytest.raises(ValueError):
        Task("", "01/01/2025")


def test_control_name_validity_not_unique():
    Task("Task", "01/01/2025")
    with pytest.raises(ValueError):
        Task("Task", "02/02/2025")


def test_control_name_validity_not_string():
    with pytest.raises(ValueError):
        Task(0, "02/02/2025")


def test_set_name():
    task1 = Task("Task 1", "01/01/2025")
    task1.set_name("New Task Name")
    assert task1.name == "New Task Name"


def test_control_date_validity_incomplete_date():
    with pytest.raises(ValueError):
        Task("Missing Year", "01/01")

    with pytest.raises(ValueError):
        Task("Invalid Day", "1/01/2025")

    with pytest.raises(ValueError):
        Task("Invalid Month", "01/1/2025")

    with pytest.raises(ValueError):
        Task("Invalid Year", "01/01/25")


def test_control_date_validity_past_date():
    with pytest.raises(ValueError):
        Task("Invalid Past Year", "01/01/1990")


def test_set_due_date():
    task2 = Task("Task 2", "01/01/2025")
    task2.set_due_date("02/02/2025")
    assert task2.due_date == datetime.datetime(2025, 2, 2)


def test_control_description_validity_length():
    with pytest.raises(ValueError):
        Task(
            "Invalid Description",
            "01/01/2025",
            "This is a too long description because its length is bigger than \
                the 100 characters authorized. Try another one.",
        )


def test_set_description():
    task3 = Task("Task 3", "01/01/2025")
    task3.set_description("New Description")
    assert task3.description == "New Description"


def test_control_completion_validity_not_integer():
    with pytest.raises(ValueError):
        Task("Invalid Type Completion", "01/01/2025", completion="1")


def test_control_completion_validity_range():
    with pytest.raises(ValueError):
        Task("Invalid Completion < 0", "01/01/2025", completion=-1)

    with pytest.raises(ValueError):
        Task("Invalid Completion > 100", "01/01/2025", completion=101)


def test_set_completion():
    task4 = Task("Task 4", "01/01/2025")
    task4.set_completion(50)
    assert task4.completion == 50


def test_get_all_tasks():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    task2 = Task("Task 2", "01/01/2025")
    all_tasks = Task.get_all_tasks()
    assert task1 in all_tasks
    assert task2 in all_tasks
    assert len(all_tasks) == 2


def test_get_todo_tasks():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    task2 = Task("Task 2", "01/01/2025", completion=100)
    task3 = Task("Task 3", "01/01/2025", completion=3)
    todo_tasks = Task.get_todo_tasks()
    assert task1 in todo_tasks
    assert task2 not in todo_tasks
    assert task3 not in todo_tasks
    assert len(todo_tasks) == 1


def test_get_doing_tasks():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    task2 = Task("Task 2", "01/01/2025", completion=100)
    task3 = Task("Task 3", "01/01/2025", completion=3)
    doing_tasks = Task.get_doing_tasks()
    assert task1 not in doing_tasks
    assert task2 not in doing_tasks
    assert task3 in doing_tasks
    assert len(doing_tasks) == 1


def test_get_done_tasks():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    task2 = Task("Task 2", "01/01/2025", completion=100)
    task3 = Task("Task 3", "01/01/2025", completion=3)
    done_tasks = Task.get_done_tasks()
    assert task1 not in done_tasks
    assert task2 in done_tasks
    assert task3 not in done_tasks
    assert len(done_tasks) == 1


def test_get_task_by_name():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    Task("Task 2", "01/01/2025")
    found_task = Task.get_task_by_name("Task 1")
    assert found_task == task1


def test_get_task_by_id():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    Task("Task 2", "01/01/2025")
    found_task = Task.get_task_by_id(task1.id)
    assert found_task == task1


def test_remove():
    Task.instances = []
    task1 = Task("Task 1", "01/01/2025")
    task2 = Task("Task 2", "01/01/2025")
    Task.remove(task1)
    assert task1 not in Task.instances
    assert task2 in Task.instances
