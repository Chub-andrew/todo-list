from django.urls import path

from todo.views import (
    TagListView, TaskListView, TagCreateView,
    TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagUpdateView, TagDeleteView, change_status
)

urlpatterns = [
    path("tags/", TagListView.as_view(),
         name="tag_list"),
    path("", TaskListView.as_view(),
         name="task_list"),
    path("tags/create/", TagCreateView.as_view(),
         name="tag_create"),
    path("create/", TaskCreateView.as_view(),
         name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(),
         name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task_delete"),
    path("tags/<slug:slug>/update/", TagUpdateView.as_view(),
         name="tag_update"),
    path("tags/<slug:slug>/delete/", TagDeleteView.as_view(),
         name="tag_delete"),
    path("<int:pk>/change_status/", change_status,
         name="change_status"),
]

app_name = "todo"
