from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(label="Enter the name of the task: ")
    detail = forms.CharField(
        label="Enter the details of your task: ", widget=forms.Textarea
    )
