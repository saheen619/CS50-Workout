# To collect 3 names
"""
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in names:
    print(f"Hello, {name}")
"""


"""
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""



# The same can be coded using a with statement

name = input("What's your name? ")

with open("names.txt", 'a') as file:
    file.write(f"{name}\n")

file.close()