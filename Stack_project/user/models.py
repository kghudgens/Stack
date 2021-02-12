from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tagline = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Username: {self.user}"
