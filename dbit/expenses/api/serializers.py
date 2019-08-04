from rest_framework import serializers

from dbit.expenses.api.models import Expenses


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"
