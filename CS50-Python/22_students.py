"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
"""



# to have the above output in sorted order,
"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
"""



# ANother approach
"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""



# Sorting the output
# Here the output is sorted by line
"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
"""




# To sort students by their name, we use a dictionary and append name and houses seperately to the list
"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name):
    print(f"{student['name']} is in {student['house']})")
"""





# Doing the same above code using a lambda function, because we use the function only once

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")