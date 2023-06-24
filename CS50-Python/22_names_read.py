"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())
"""



# The above code canb be make compact as :
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())
"""



names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")