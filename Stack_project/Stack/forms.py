from django import forms


class StockForm(forms.Form):
    name = forms.CharField(label="Enter the name of the task: ")
    detail = forms.CharField(
        label="Enter the details of your task:", widget=forms.Textarea
    )
    date_created = forms.DateTimeField()
