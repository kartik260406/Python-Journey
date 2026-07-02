# Project - Result Calculator

## What I built
- grade.py — Student Class to create result of each student in file using marks from another file with 
                1 - properties(data,avg,grade,result)
                2 - classmethod(get)
             — File I/O to read and write in files using Dictreader and Dictwriter of CSV
             — Error Handling used for marks and file validation & raise Value Error on required inputs

## What I learned
- File I/O — reading and writing files using open(), and CSV files with DictReader and DictWriter
- Error Handling — try/except, raise
- OOP — classes, __init__, properties, classmethods,__str__

## Sample CSV Format

**Input (e.g. students.csv)**
```
name,marks1,marks2,marks3
Alice,85,90,78
Bob,45,50,40
```

**Output (e.g. results.csv)**
```
Name,Average_Marks,Grade,Result
Alice,84.33,B,Pass
Bob,45.0,E,Pass
```

## How to run
```
python grade.py
```

## Tech used
Python 3.12