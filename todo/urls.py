from django.urls import path

from todo.views import index


urlpatterns = [
    path('', index),
    path('hello/', index),
]

app_name = "todo"