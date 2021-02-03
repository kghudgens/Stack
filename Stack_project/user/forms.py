from django import forms
from .models import *


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="Enter your first name", max_length=30)
    last_name = forms.CharField(label="Enter your last name", max_length=30)
    tagline = forms.CharField(label="Enter a tagline", max_length=100)

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "tagline", "image"]
