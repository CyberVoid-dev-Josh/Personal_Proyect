
name = input("Insert full name: ")
student_grade = int(input("Insert studet grade: "))

limit_grade = 60

if student_grade >= 60:
    print(name, ": Passed")
if  student_grade <= 60:
    print(name, ": Failed")
