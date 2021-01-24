from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import TaskForm


def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your task has been added")
            return HttpResponseRedirect("/index/")
    else:
        form = TaskForm()
    return render(request, "Stack/index.html", {"form": form})
