from rest_framework import serializers
from apps.accounting_app.models import IncomeDetailModel, OutcomeDetailMode

class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeDetailModel
        fields = ['name_income', 'total_income', 'income_type', 'updated_at']

class OutComeSerializer(serializers):

    class Meta:
        model = OutcomeDetailMode
        fields = ['name_outcome', 'total_outcome', 'outcome_type', 'updated_at']
