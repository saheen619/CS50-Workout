import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Slytherin", "Ravenclaw"]
        
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")