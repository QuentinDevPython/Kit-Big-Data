"""Views for tasks."""

from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import PositionForm
from .models import Task


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
        """
        Get the URL to redirect to after successful login.
        """
        return reverse_lazy('tasks')


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
        """
        Add additional context data to the view.
        """
        context = super().get_context_data(**kwargs)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input
            )

        context['search_input'] = search_input
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
        """
        Validate and save the form for task creation.
        """
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


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


class TaskReorder(View):
    """
    View for reordering tasks.

    Methods:
        post(request): Handle the task reordering request.
    """

    def post(self, request):
        """
        Handle the task reordering request.

        Parameters:
            request: The HTTP request object.

        Returns:
            HttpResponse: A response after reordering the tasks.
        """
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))
