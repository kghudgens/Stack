from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.edit import FormView
from .models import Profile
from .forms import ProfileUpdateForm


class UpdateProfileView(FormView):
    template_name = "update_profile.html"
    form_class = ProfileUpdateForm
    success_url = "/profile/"

    def form_valid(self, form):
        return super().form_valid(form)


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
    context = {"profile": Profile.objects.all()}
    return render(request, "user/update_profile.html", context)
