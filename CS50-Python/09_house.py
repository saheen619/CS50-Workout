"""
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherine")
else:
    print("Who??")
"""


# Better code
"""
name = input("What's your name? ")

if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherine")
else:
    print("Who??")
"""



# Using match keyword in latest python
"""
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who ??")
"""


# Concising Same house member names
name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who ??")