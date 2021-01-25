from django.db import models


class TaskManager(models.Model):
    task_name = models.CharField(max_length=30)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name