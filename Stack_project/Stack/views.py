from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import TaskForm


def index(request):
    return render(request, "Stack/index.html")


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your task has been added")
            return redirect("index")
    else:
        form = TaskForm()
    return render(request, "Stack/create.html", {"form": form})
