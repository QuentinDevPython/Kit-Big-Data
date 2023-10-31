"""Views for tasks."""

import logging
from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import PositionForm
from .models import Task

# Create a logger instance for error and critical logs
error_logger = logging.getLogger('error_logger')

# Create a logger instance for debug logs
debug_logger = logging.getLogger('debug_logger')


class CustomLoginView(LoginView):
    """
    Custom login view for user authentication.

    Attributes:
        template_name (str): The path to the login template.
        fields (str): The fields used for authentication.
        redirect_authenticated_user (bool): Redirect authenticated users.

    Methods:
        get_success_url(): Get the URL to redirect to after successful login.
    """

    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """Get the URL to redirect to after successful login."""
        url = reverse_lazy('tasks')

        # Log a debug message
        log_message = (
            f"Successful login for user: {self.request.user.username}")
        debug_logger.debug(log_message)

        return url

    def form_valid(self, form):
        """Form valid method."""
        log_message = f"User '{self.request.user}' has logged in."
        debug_logger.debug(log_message)

        return super().form_valid(form)

    def form_invalid(self, form):
        """Form invalid method."""
        log_message = (
            "Failed login attempt for user: "
            f"{form.cleaned_data['username']}"
        )
        error_logger.error(log_message)

        return super().form_invalid(form)


class TaskList(LoginRequiredMixin, ListView):
    """
    View for listing tasks for a logged-in user.

    Attributes:
        model: The model used for the view.
        context_object_name (str): The name to use for the context object.
        template_name (str): The path to the template for rendering the view.

    Methods:
        get_context_data(**kwargs): Add additional context data to the view.
    """

    model = Task
    context_object_name = 'tasks'
    template_name = 'your_template_name.html'  # Specify the template name

    def get_context_data(self, **kwargs):
        """Add additional context data to the view."""
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete=False).count()
        try:
            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tasks'] = context['tasks'].filter(
                    title__startswith=search_input
                )

                # Log a debug message for search
                debug_logger.debug(
                    "TaskList search result for input '%s': %s",
                    search_input, context['tasks'])

            context['search_input'] = search_input
        except Exception as e:
            # Log the error and critical message
            error_logger.error("Error during TaskList view: %s", str(e))

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    """
    View for displaying details of a task.

    Attributes:
        model: The model used for the view.
        context_object_name (str): The name to use for the context object.
        template_name (str): The path to the template for rendering the view.
    """

    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """
    View for creating a new task.

    Attributes:
        model: The model used for the view.
        template_name (str): The path to the template for rendering the view.
        fields (list): The fields to include in the form.
        success_url: The URL to redirect to after successful form submission.

    Methods:
        form_valid(form): Validate and save the form for task creation.
    """

    model = Task
    template_name = 'tasks/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        """Form valid method."""
        try:
            # Custom logic here
            form.instance.user = self.request.user

            # Log a debug message
            log_message = (
                f"TaskCreate form valid - User: {self.request.user}, "
                "Form Data: {form.cleaned_data}"
            )
            debug_logger.debug(log_message)
            return super(TaskCreate, self).form_valid(form)
        except Exception as e:
            # Log the error and critical message
            error_logger.error("Error during task creation: %s", str(e))
            return HttpResponseServerError()


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing task.

    Attributes:
        model: The model used for the view.
        fields (str): The fields to include in the form.
        success_url: The URL to redirect to after successful form submission.
    """

    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """Form valid method."""
        try:
            # Get the task to be updated
            task = self.get_object()

            # Log a debug message before updating
            log_message = (
                f"TaskUpdate form valid - Task: {task} , "
                "Form Data: {form.cleaned_data}"
            )
            debug_logger.debug(log_message)

            # Perform the form submission
            return super(TaskUpdate, self).form_valid(form)
        except Exception as e:
            # Log the error and critical message if an error occurs
            error_logger.error("Error during task update: %s", str(e))
            return HttpResponseServerError()


class DeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting a task.

    Attributes:
        model: The model used for the view.
        context_object_name (str): The name to use for the context object.
        success_url: The URL to redirect to after successful deletion.
    """

    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        try:
            # Get the task to be deleted
            task = self.get_object()

            # Log a debug message before deleting
            debug_logger.debug("TaskDelete deleting task: %s", task)

            # Perform the actual deletion
            task.delete()

            # Log a success message after deletion
            debug_logger.debug("Task deleted successfully: %s", task)

            return redirect(self.success_url)
        except Exception as e:
            # Log the error and critical message if an error occurs
            error_logger.error("Error during task deletion: %s", str(e))
            return HttpResponseServerError()


class TaskReorder(View):
    """
    View for reordering tasks.

    Methods:
        post(request): Handle the task reordering request.
    """

    def post(self, request):
        try:
            form = PositionForm(request.POST)
            if form.is_valid():
                positionList = form.cleaned_data["position"].split(',')

                with transaction.atomic():
                    self.request.user.set_task_order(positionList)

                # Log a debug message
                debug_logger.debug("TaskReorder successful")
                return redirect(reverse_lazy('tasks'))
        except Exception as e:
            # Log the error and critical message
            error_logger.error("Error during task reordering: %s", str(e))
            return HttpResponseServerError()
