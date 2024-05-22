from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    queryset = Tag.objects.all()
    context_object_name = "tags"
    success_url = reverse_lazy("todo:tag_list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    success_url = reverse_lazy("todo:task_list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag_list")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag_list")


def change_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse("todo:task_list"))
