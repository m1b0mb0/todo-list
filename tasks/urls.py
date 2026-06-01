from django.urls import path

from tasks.views import TaskListView, TagListView, TaskCreateView


app_name = "tasks"

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
