"""Urls for tasks."""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasklist, name='tasks'),
]
