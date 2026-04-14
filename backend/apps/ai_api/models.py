from django.db import models

# Create your models here.

class Preferences(models.Model):
    city_state = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    recipe = models.TextField(blank=True)

class Output(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField(blank=True)