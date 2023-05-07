from django.contrib import admin
from apps.accounting_app.models import IncomeType, OutcomeType, IncomeDetailModel, OutcomeDetailMode
# Register your models here.
@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "code_finance"]

@admin.register(OutcomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "code_finance"]

@admin.register(IncomeDetailModel)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ["name_income",
                    "total_income",
                    "income_type",
                    "updated_at",
                    "created_at",
                    ]

@admin.register(OutcomeDetailMode)
class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ["name_outcome",
                    "total_outcome",
                    "outcome_type",
                    "updated_at",
                    "created_at",
                    ]

