from django.db import models
from django.contrib.auth.models import AbstractUser

class AccountAdmin(AbstractUser):

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = "account_admin"

class DateTimeModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField()