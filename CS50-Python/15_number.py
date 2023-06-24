# Error Handling


"""
x = int(input("What's X? "))
print(f"x is {x}")
"""


# What if the user inputs a string as input?

"""
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
"""


"""
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""


# To prompt the user for an input until the user enters a valid input,

"""
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer. input an integer to continue")
    else:
        break

print(f"x is {x}")
"""



# Having the same inside a function
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer. input an integer to continue")
        else:
            return x

main()
"""



# The above code could be further refined as

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer. input an integer to continue")

main()


# MNaking the code more dynamic within the function

"""
def main():
    x = get_int("What's x ? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer. input an integer to continue")

main()
"""
