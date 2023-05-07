from django.urls import path
from apps.accounting_app.views import AllIncomeView, AllOutcomeView
urlpatterns = [
    path('all_income/', AllIncomeView.as_view(), name='all_income'),
    path('all_outcome/', AllOutcomeView.as_view(), name="all_outcome")
]