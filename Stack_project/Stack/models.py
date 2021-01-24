from django.db import models

# Create your models here.
class TaskManager(models.Model):
    task_name = models.CharField(max_length=30)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)