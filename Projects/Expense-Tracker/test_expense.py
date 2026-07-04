import pytest
from expense import Expense

def test_filter_by_category():
    e = Expense("test_data.csv", "View Expenses")
    result = e.filter_by_category("food")
    assert result[0]["category"] == "food"

def test_total_by_category():
    e = Expense("test_data.csv", "View Expenses")
    result = e.total_by_category("food")
    assert result == 800.0 

def test_invalid_task():
    with pytest.raises(ValueError):
        Expense("test_data.csv", "Wrong Task")

def test_file_not_found():
    with pytest.raises(ValueError):
        Expense("nonexistent.csv", "View Expenses")

def test_amount_property():
    e = Expense("test_data.csv", "View Expenses")
    assert e.amount == 1000.0  # 500 + 200 + 300

def test_invalid_file_extension():
    with pytest.raises(ValueError):
        Expense("test_data.txt", "View Expenses")