"""Data models for tasks."""

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Model representing a task.

    Attributes:
        user (ForeignKey to User): The user associated with the task.
        title (CharField): The title of the task, max length 200 characters.
        description (TextField): A detailed description of the task.
        complete (BooleanField): Indicates if the task is completed or not.
        created (DateTimeField): The date and time when the task was created.
        due_date (DateField, optional): The due date for the task.

    Methods:
        __str__(): A string representation of the task, returns the title.

    Meta:
        ordering (list): Default order of tasks, sorted by 'complete' status.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Establishes a one-to-many relationship where a user can have multiple tasks.
    # The `models.CASCADE` ensures that if the user is deleted, their tasks are deleted.

    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        """
        returns the title.
        """
        return self.title

    class Meta:
        """
        Metadata for the Task model.
        """

        ordering = ["complete"]
