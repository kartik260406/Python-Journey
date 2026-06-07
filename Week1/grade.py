import statistics
def get_marks(prompt):
    while True:
        try:
            marks = float(input(f"Enter the valid marks of {prompt}: "))
        except ValueError:
            print("Invalid Number")
        else:
            if marks<0 or marks>100:
                print("Marks are out of range")
            else:
                return marks

def main():    
    name = input("Enter your Name: ").strip()
    sub1 = get_marks("Subject 1")
    sub2 = get_marks("Subject 2")
    sub3 = get_marks("Subject 3")
    avg = statistics.mean(sub1,sub2,sub3)
    print(f"Name: {name}")
    print(f"Average Marks: {avg:.2f}")
    print("Your Grade:",calc_grade(avg))
    print(calc_result(avg))

def calc_grade(avg):
    if avg<0 or avg>100:
        raise ValueError
    elif avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=40:
        return "D"
    else:
        return "F"
    
def calc_result(avg):
    if avg<0 or avg>100:
        raise ValueError
    elif avg>=40:
        return "Result: Pass"
    else:
        return "Result: Fail"

if __name__== "__main__":
    main()