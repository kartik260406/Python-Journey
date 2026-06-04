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
    avg = (sub1 + sub2 + sub3)/3
    print(f"Name: {name}")
    print(f"Average Marks: {avg:.2f}")
    print("Your Grade:",end = " ")
    if avg>=90:
        print("A")
    elif avg>=80:
        print("B")
    elif avg>=70:
        print("C")
    elif avg>=40:
        print("D")
    else:
        print("F")
    if avg>=40:
        print("Result: Pass")
    else:
        print("Result: Fail")

main()