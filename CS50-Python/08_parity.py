"""
def main():
    number = int(input("What's x? "))
    oddoreven(number)

def oddoreven(x):
    if x % 2 == 0:
        print("x is an EVEN number")
    else:
        print("x is an ODD number")

main()
"""


# Another approach

def main():
    number = int(input("What's x? "))
    if oddoreven(number) == True:
        print("EVEN")
    else:
        print("ODD")

def oddoreven(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()



# Another better approach
"""
def main():
    number = int(input("What's x? "))
    if oddoreven(number) == True:
        print("EVEN")
    else:
        print("ODD")

def oddoreven(n):
    return n % 2 == 0

main()
"""