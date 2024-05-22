from django.db import models
from django.urls import reverse


class Task(models.Model):
    content = models.TextField()
    create_task = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        null=True,
        unique=True,
        blank=False
    )

    class Meta:
        ordering = ("name", )
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name
