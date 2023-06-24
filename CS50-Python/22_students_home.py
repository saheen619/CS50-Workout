# Go through the student_home.csv and you will find an additional , on parameter
# To solve this, we import a csv module in python and use the reader method

"""
import csv

students = []

with open("students_home.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home" : home})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""




# TO make the code more robust and dynamic:
# By using csv.DictReader method to read the raw file and dynamically assign values to the columns
# also note that the columns in order has been changed in the csv file

import csv

students = []

with open("students_home2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"], "home" : row["home"]})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")