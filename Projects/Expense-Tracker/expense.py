import csv
import sys
import re
from pathlib import Path

class Expense:
    def __init__(self,file,task):
        valid_task = ["Add Expense","View Expenses","Delete Expense"]
        if task not in valid_task:
            raise ValueError("Wrong task Value")
        self.is_file_valid = valid(file,task)
        if not self.is_file_valid:
            self._amount = 0
        self._file = file
        if task == valid_task[1]:
            data = self.view
            if data == []:
                print("No expense found")
            else:
                for expense in data:
                    print(expense)
        else:
            try:
                amt = float(input("Enter the amount: "))
                if amt<0:
                    raise ValueError("Invalid Amount Entered")
            except ValueError:
                print("Invalid Amount Value")
                sys.exit()
            ctg = input("Enter the Category: ")
            date = input("Enter the Date in 'dd-mm-yyyy' format only: ")
            if not re.search(r"(\d\d)\-(\d\d)\-(\d\d\d\d)",date):
                raise ValueError("Wrong Date")
            desc = input("Enter the Description: ")
            if not ctg or not desc:
                raise ValueError("Invalid Value")
            expense_data = {"amount":amt,"category":ctg,"date":date,"description":desc}
            if task == valid_task[0]:
                self.add(expense_data)
            elif task == valid_task[2]:
                self.delete(expense_data)

    @property
    def amount(self):
        if not self.is_file_valid:
            return self._amount
        args = self.view
        amt = 0
        for i in args:
            amt += float(i["amount"])
        if amt<0:
            raise ValueError("Wrong Values")
        return amt

    @property
    def view(self):
        if not self.is_file_valid:
            raise ValueError("Can't apply delete at empty file")
        data = []
        with open(self._file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({"amount":row["amount"],"category":row["category"],"date":row["date"],"description":row["description"]})
        return data

    def add(self,line):
        if not self.is_file_valid:
            with open(self._file,"w") as file:
                writer = csv.DictWriter(file,fieldnames=["amount","category","date","description"])
                writer.writeheader()
                writer.writerow({"amount":line["amount"],"category":line["category"],"date":line["date"],"description":line["description"]})
        else:
            with open(self._file,"a") as file:
                writer = csv.DictWriter(file,fieldnames=["amount","category","date","description"])
                writer.writerow({"amount":line["amount"],"category":line["category"],"date":line["date"],"description":line["description"]})
        
    def delete(self,line):
        if not self.is_file_valid:
            raise ValueError("Can't apply delete at empty file")
        data = self.view
        if data == []:
            raise ValueError("File is empty")
        with open(self._file,"w") as file:
            writer = csv.DictWriter(file,fieldnames=["amount","category","date","description"])
            writer.writeheader()
            for expense in data:
                if expense != line:
                    writer.writerow(expense)
        
    @classmethod
    def get(cls):
        file = input("Enter the name of file: ").strip()
        task = input("Which task you want to do?\n 1. Add Expense\n 2. View Expenses\n 3. Delete Expense\n Enter Choice: ").strip()
        mapping = {"1":"Add Expense","2":"View Expenses","3":"Delete Expense"}
        if task not in mapping:
            raise ValueError("Invalid choice")
        return cls(file,mapping[task])
    
def valid(file,task):
    if not file.endswith(".csv"):
        raise ValueError("Wrong Input File")
    file_path = Path(file)
    if not file_path.is_file():
        if task == "Add Expense":
            return False
        else:
            raise ValueError("File Not Found")
    return True