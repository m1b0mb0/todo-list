from django.urls import path

from tasks.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TagListView,
)


app_name = "tasks"

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]
