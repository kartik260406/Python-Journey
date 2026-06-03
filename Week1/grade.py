Name = input("Enter your Name: ").strip()
Sub1 = float(input("Enter the marks of subject 1: "))
while Sub1 < 0 or Sub1 > 100:
    Sub1 = float(input("Enter the valid marks of subject 1: "))
Sub2 = float(input("Enter the marks of subject 2: "))
while Sub2 < 0 or Sub2 > 100:
    Sub2 = float(input("Enter the valid marks of subject 2: "))
Sub3 = float(input("Enter the marks of subject 3: "))
while Sub3 < 0 or Sub3 > 100:
    Sub3 = float(input("Enter the valid marks of subject 3: "))
Avg = (Sub1 + Sub2 + Sub3)/3
print(f"Name: {Name}")
print(f"Average Marks: {Avg}")
print("Your Grade:",end = " ")
if Avg>=90:
    print("A")
elif Avg>=80:
    print("B")
elif Avg>=70:
    print("C")
elif Avg>=40:
    print("D")
else:
    print("F")
if Avg>=40:
    print("Result: Pass")
else:
    print("Result: Fail")