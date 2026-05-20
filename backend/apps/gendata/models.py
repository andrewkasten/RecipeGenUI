from django.db import models

# Create your models here.
# explanation

class Output(models.Model):
    variant = models.JSONField(null=True, blank=True, default=dict)
    explanation = models.JSONField(null=True, blank=True, default=dict)

