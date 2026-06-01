from django.views import generic
from django.urls import reverse_lazy

from tasks.models import Task, Tag
from tasks.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
