from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Your account has been created {username}")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})


def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been updated.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm()
    return render(request, "user/profile.html", {"form": form})
