import pytest

from dbit.expenses.api.models import Expenses


class TestExpenseModel:
    @pytest.fixture
    def expense(self):
        valid_expense = {
            "name": "test_expense",
            "description": "This is a expense description",
            "value": 49.99,
        }
        return valid_expense

    @pytest.mark.django_db
    def test_create_expense(self, expense):
        new_expense = Expenses(**expense)
        new_expense.save()
        assert isinstance(new_expense, Expenses)
        assert new_expense.name == expense["name"]

    @pytest.mark.django_db
    def test_create_invalid_expense_should_raise_exeption(self, expense):
        expense["value"] = "invalid_value"
        new_expense = Expenses(**expense)
        with pytest.raises(ValueError):
            new_expense.save()
            assert isinstance(new_expense, Expenses)
