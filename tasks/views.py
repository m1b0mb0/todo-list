from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from tasks.models import Task, Tag
from tasks.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


def toggle_task_status(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()

        return redirect("tasks:task-list")
