from django.db import models
from apps.common.models import DateTimeModel

# Create your models here.
class IncomeType(models.Model):
    name = models.CharField(max_length=500)
    code_finance = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class OutcomeType(models.Model):
    name = models.CharField(max_length=500)
    code_finance = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class IncomeDetailModel(DateTimeModel, models.Model):
    name_income = models.CharField(max_length=500)
    total_income = models.IntegerField()
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)

class OutcomeDetailModel(DateTimeModel, models.Model):
    name_outcome = models.CharField(max_length=500)
    total_outcome = models.IntegerField()
    outcome_type = models.ForeignKey(OutcomeType, on_delete=models.CASCADE)