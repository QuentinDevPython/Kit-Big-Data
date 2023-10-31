"""Test file for the django app."""
import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from .views import (
    TaskList, TaskDetail, TaskCreate, TaskUpdate,
    DeleteView, CustomLoginView, TaskReorder
)
from .forms import PositionForm

class TaskModelTestCase(TestCase):
    """Test case for the Task model."""

    def setUp(self):
        """Set up test data for the model tests."""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
            )

    def test_task_creation(self):
        """Test creating a task instance."""
        task = Task.objects.create(
            user=self.user, title="Test Task", 
            description="Description", complete=False, due_date="2023-12-31"
            )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertFalse(task.complete)
        self.assertEqual(task.due_date, "2023-12-31")
        self.assertEqual(task.user, self.user)

    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task.objects.create(user=self.user, title="Another Task")
        self.assertEqual(str(task), "Another Task")

    def test_task_ordering(self):
        """Test the ordering of tasks."""
        task1 = Task.objects.create(user=self.user, title="Task 1", complete=False)
        task2 = Task.objects.create(user=self.user, title="Task 2", complete=True)

        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task1)  # Uncompleted tasks should come first

    def test_task_user_deletion(self):
        """Test user deletion and associated task deletion."""
        task = Task.objects.create(user=self.user, title="Task to be deleted")
        user_id = self.user.id
        self.user.delete()  # Deleting the user should also delete associated tasks
        task_exists = Task.objects.filter(user_id=user_id).exists()
        self.assertFalse(task_exists)

    def test_task_defaults(self):
        """Test the default values for a task."""
        task = Task.objects.create(user=self.user)
        self.assertEqual(task.title, None)
        self.assertEqual(task.description, None)
        self.assertFalse(task.complete)
        self.assertEqual(task.due_date, None)

class TaskViewsTestCase(TestCase):
    """Test case for views related to tasks."""

    def setUp(self):
        """Set up test data for the view tests."""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.task = Task.objects.create(title="Test Task", user=self.user)

    def test_task_list_view(self):
        """Test the task list view."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_list.html")

    def test_task_detail_view(self):
        """Test the task detail view."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task.html")

    def test_task_create_view(self):
        """Test the task create view."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("task-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_update_view(self):
        """Test the task update view."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("task-update", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_delete_view(self):
        """Test the task delete view."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("task-delete", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_confirm_delete.html")

class TaskFormTestCase(TestCase):
    """Test case for the PositionForm form."""

    def setUp(self):
        """Set up test data for the form tests."""
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_position_form_valid(self):
        """Test a valid PositionForm instance."""
        form_data = {"position": "1,2,3"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())

class CustomLoginViewTestCase(TestCase):
    """Test case for the CustomLoginView view."""

    def test_custom_login_view(self):
        """Test the custom login view's response and template."""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/login.html")

    def test_custom_login_view_success_url(self):
        """Test the custom login view's success URL."""
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("tasks"))
        self.assertRedirects(response, reverse("tasks"))

if __name__ == '__main__':
    unittest.main()
