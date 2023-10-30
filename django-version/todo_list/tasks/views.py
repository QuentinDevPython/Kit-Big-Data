"""Views for tasks."""

# from django.shortcuts import render
from django.http import HttpResponse


def tasklist(request):
    """Test view."""
    return HttpResponse('To Do list')
