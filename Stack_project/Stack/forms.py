from django.forms import ModelForm
from .models import TaskManager


class TaskForm(ModelForm):
    class Meta:
        model = TaskManager
        fields = ["task_name", "detail"]


form = TaskForm()
