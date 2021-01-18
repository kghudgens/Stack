from django.db import models

# Create your models here.
class StockInformation(models.Model):
    name = models.CharField(max_length=30)
    ticker = models.CharField(max_length=10)
