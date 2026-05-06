from django.db import models

# Create your models here.

class Recipe(models.Model):
    state = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    recipe = models.JSONField(null=True, blank=True, default=dict)