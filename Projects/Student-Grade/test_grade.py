import pytest
from grade import Student

def test_avg():
    s = Student("test_students.csv", "test_output.csv")
    assert s.avg["Alice"] == 90.0
    assert s.avg["Bob"] == 30.0
    assert s.avg["Charlie"] == 75.0

def test_grade():
    s = Student("test_students.csv", "test_output.csv")
    assert s.grade["Alice"] == "A"
    assert s.grade["Bob"] == "F"
    assert s.grade["Charlie"] == "C"

def test_result():
    s = Student("test_students.csv", "test_output.csv")
    assert s.result["Alice"] == "Pass"
    assert s.result["Bob"] == "Fail"
    assert s.result["Charlie"] == "Pass"

def test_sorted_by_name():
    s = Student("test_students.csv", "test_output.csv")
    names = [row["name"] for row in s.data]
    assert names == sorted(names)

def test_invalid_file_extension():
    with pytest.raises(ValueError):
        Student("students.txt", "output.csv")

def test_file_not_found():
    with pytest.raises(ValueError):
        Student("nonexistent.csv", "output.csv")