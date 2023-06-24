# To print Mario Bricks
"""
for _ in range(3):
    print("#")
"""
"""
def main():
    
    number = int(input("Number of bricks: "))
    column_print(number)

def column_print(number):
    for _ in range(number):
        print("#")

main()
"""




# TO print the row of '?'
"""
def main():
    row_print(4)

def row_print(x):
    for _ in range(x):
        print("?", end = "")

main()
"""




# Print the mario square bricks, where we could consider them as 3x3:

def main():
    square_bricks(4)

def square_bricks(x):
    for _ in range(x):
        print("#" * x)

main()

# Anothe rapproch for the 3x3 brick:
"""
def main():
    square_bricks(3)

def square_bricks(x):
    for i in range(x):
        for j in range(x):
            print("#", end="")
        print()

main()
"""