import pytest
from grade import calc_result
from grade import calc_grade

def test_calc_result():
    assert calc_result(50) == "Result: Pass"
    assert calc_result(0) == "Result: Fail"

def test_calc_grade():
    assert calc_grade(20) == "F"
    assert calc_grade(100) == "A"
    assert calc_grade(60) == "D"

def test_negative_values():
    with pytest.raises(ValueError):
        calc_grade(-5)
    with pytest.raises(ValueError):
        calc_result(-8)
