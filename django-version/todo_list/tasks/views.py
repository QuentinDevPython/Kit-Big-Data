"""Views for tasks."""

#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task


class TaskList(ListView):
    """_summary_

    Args:
        ListView (_type_): _description_
    """
    model = Task
