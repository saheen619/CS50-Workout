""" def main():
    name, house = get_student()
    print(f"{name} is from {house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return name, house

if __name__ == "__main__":
    main() """




# ANother approach - Instead of default tuples, we use dictionary, since we wanted to change the value of padma as a studnet
""" 
def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "Ravenclow"
    print(f"{student['name']} is from {student['house']}")

def get_student():
    name = input("Name: ")
    hosue = input("House: ")
    return {"name":name, "house":house}

if __name__ == "__main__":
    main()
 """





 # Changing the above code by creating a class. We're removing the dictionary and rewriting code as per the class and its attributes.

class Student:
    def __init__ (self, name, house):
        self.name = name
        self.house = house

    def __str__ (self):
        return f"{self.name} is from {self.house}"
    
    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError ("Missing Name")
        self._name = name


    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff","Slytherin","Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(student)
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()