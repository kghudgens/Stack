from django.db import models
from django.contrib.auth.models import User


class TaskManager(models.Model):
    task_name = models.CharField(max_length=30)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name