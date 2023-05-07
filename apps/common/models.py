from django.db import models

# Create your models here.
class DateTimeModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField()