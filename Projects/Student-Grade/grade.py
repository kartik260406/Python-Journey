import csv
from pathlib import Path
class Student:
    def __init__(self,i_file,o_file):
        if not i_file.endswith(".csv") or not o_file.endswith(".csv"):
            raise ValueError("Wrong csv file names")
        file_path = Path(i_file)
        if not file_path.is_file():
            raise ValueError("Input File Not Found")
        self.i_file = i_file
        self.o_file = o_file

    def __str__(self):
        students_avg = self.avg
        students_grade = self.grade
        student_result = self.result
        with open(self.o_file,"w") as file:
            writer = csv.DictWriter(file,fieldnames=["Name","Average_Marks","Grade","Result"])
            writer.writeheader()
            for name in students_avg:
                writer.writerow({"Name":name,"Average_Marks":students_avg[name],"Grade":students_grade[name],"Result":student_result[name]})
        return f"Result written to {self.o_file}"
    
    @classmethod
    def get(cls):
        input_file = input("Enter Input File Name: ")
        output_file = input("Enter Output File Name: ")
        return cls(input_file,output_file)
    
    @property
    def data(self):
        students = []
        with open(self.i_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row["name"]:
                    raise ValueError("Wrong Name")
                if not all(0 <= int(row[m]) <= 100 for m in ["marks1","marks2","marks3"]):
                    raise ValueError("Wrong Marks")
                students.append(row)
        students = sorted(students,key= lambda student:student["name"])
        return students
    
    @property
    def avg(self):
        info = self.data
        avg_marks = {}
        for data in info:
            avg_marks[data["name"]] = round((int(data["marks1"])+int(data["marks2"])+int(data["marks3"]))/3,2)
        return avg_marks

    @property
    def grade(self):
        grade_student = {}
        info = self.avg
        for i in info:
            if info[i] >= 90:
                grade_student[i] = "A"
            elif info[i] >=80:
                grade_student[i] = "B"
            elif info[i] >=70:
                grade_student[i] = "C"
            elif info[i] >=60:
                grade_student[i] = "D"
            elif info[i] >=40:
                grade_student[i] = "E"
            else:
                grade_student[i] = "F"
        return grade_student
    
    @property
    def result(self):
        result_student = {}
        info = self.avg
        for i in info:
            if info[i]<40:
                result_student[i] = "Fail"
            else:
                result_student[i] = "Pass"
        return result_student
    
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()