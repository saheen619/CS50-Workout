"""
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y or x < y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""



# Better Approach - More efficient Code - Less complexity (You could identify the complexity using a flow chart/ control diagram)
# The computer answers fewer questions in this case by limitting the number of questions(if and ifelse) asked

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")