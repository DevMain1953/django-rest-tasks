from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255, default="Simple task")
    text = models.TextField()

    STATES = [("accepted", "Accepted"), ("in_process", "In process"), ("finished", "Finished")]
    state = models.CharField(choices=STATES, max_length=10)
    author = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    PRIORITY = [("high", "High"), ("medium", "Medium"), ("low", "Low")]
    priority = models.CharField(choices=PRIORITY, max_length=6)

    class Meta:
        verbose_name_plural = "tasks"