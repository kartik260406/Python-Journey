# Project - Expense Calculator

## What I built
- expense.py — Expense Class with 
                1 - properties(amount,view)
                2 - methods(add,delete,filter by category,total expense on category)
                3 - classmethod(get)
             — File I/O to read and write in files using Dictreader and Dictwriter of CSV
             — Regex used for validation of date by re.search
             — Error Handling used for amount validation & raise Value Error on required inputs

## What I learned
- File I/O — reading and writing files using open(), and CSV files with DictReader and DictWriter
- Regex — re.search()
- Error Handling — try/except, raise
- OOP — classes, __init__, properties, classmethods

## Sample CSV Format
```
amount,category,date,description
500,food,13-06-2025,lunch
```

## How to run
```
python expense.py
```

You'll be asked for a CSV filename, then choose from:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Filter By Category
5. Total Expense On Category

## Tech used
Python 3.12