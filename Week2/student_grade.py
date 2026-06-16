class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks = [marks1,marks2,marks3]

    def __str__(self):
        return f"{self.name} is {self.result} with {self.grade} grade and {self.avg} average marks"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Enter Valid Name")
        self._name = name

    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self,values):
        marks1,marks2,marks3 = values
        if not all(m in range(0,101) for m in [marks1,marks2,marks3]):
            raise ValueError("Marks are out of range")
        self._marks = [marks1,marks2,marks3]
    
    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        marks1 = int(input("Enter marks of subject 1 between 0 and 100: "))
        marks2 = int(input("Enter marks of subject 2 between 0 and 100: "))
        marks3 = int(input("Enter marks of subject 3 between 0 and 100: "))
        return cls(name,marks1,marks2,marks3)
    
    @property
    def avg(self):
        return round(sum(self.marks)/3,2)
    
    @property
    def grade(self):
        if self.avg >= 90:
            return "A"
        elif self.avg >=80:
            return "B"
        elif self.avg >=70:
            return "C"
        elif self.avg >=60:
            return "D"
        elif self.avg >=40:
            return "E"
        else:
            return "F"
    
    @property
    def result(self):
        if self.avg<40:
            return "Fail"
        else:
            return "Pass"