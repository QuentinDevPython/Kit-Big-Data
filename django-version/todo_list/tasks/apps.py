"""Apps for tasks."""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """Config for tasks app."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "tasks"
