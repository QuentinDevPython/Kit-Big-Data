"""Admin for tasks."""

from django.contrib import admin
from .models import Task

admin.site.register(Task)
