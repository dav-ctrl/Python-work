with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# Sorted

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for students in sorted(students):
    print(student)

#

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student['name']

for student in sorted(students, key=get_name):
    print(f"student['name'] is in student['house']")

##

for student in sorted(students, key = lambda student: student['name'])
    print(f"student['name'] is in student['house']")

