from django.db import models

# Create your models here.

class Preferences(models.Model):
    state = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    recipe = models.JSONField(null=True, blank=True, default=dict)

class Output(models.Model):
    input = models.CharField(max_length=255)
    output = models.TextField(blank=True)

class WeatherNote(models.Model)   :
    zip_code = models.CharField(max_length=255, default = "84062")
    note = models.TextField(blank=True)