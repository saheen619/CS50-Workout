students = [
    {"Name" : "Hermoine", "house": "Gryffindor"},
    {"Name" : "Harry", "house": "Gryffindor"},
    {"Name" : "Ron", "house": "Gryffindor"},
    {"Name" : "Draco", "house": "Slytherin"},
    {"Name" : "Padma", "house": "Ravenclaw"},
    {"Name" : "Saheen", "house": "Hufflepuff"}
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)