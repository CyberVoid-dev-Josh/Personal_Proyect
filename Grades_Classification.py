name = input("Insert student full name: ")
grade = int(input("Insert grade: "))

if grade >= 80:
    print(name, ": Approved")
elif grade >= 60:
    print(name, ": Approved")
elif grade == 45:
    print(name, ": Postponed")
else:
    print(name, ": Reproved") 