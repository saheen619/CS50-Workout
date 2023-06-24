"""
i = 3
while i != 0:
    print("meow")
    i = i -1
"""

# Another Logic
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

# Using a for loop
"""
for i in [1,2,3]:
    print("meow")
"""

# Making it dynamic
"""
for i in range(3):
    print("meow")
"""

# Anothe Approach
"""
print("meow" * 3)
"""

# with nextline
"""
print("meow\n" * 3)     # But produces one empty line
"""

# Som we use end as a parameter for the print statement
"""
print("meow\n" * 3, end="")
"""


# While dynamically recieving an input from the user, to avoid any negetive input,
"""
while True:
    n = int(input("What's x? "))
    if n > 0:
        break
        
for i in range(n):
    print("meow")
"""


# In the above code, since we do not have ant use in declaring a variable i, we use _
"""
while True:
    n = int(input("What's x? "))
    if n > 0:
        break
        
for _ in range(n):
    print("meow")
"""


# Lets make this into a function

def main():
    x = get_number()
    meow(x)

def get_number():    
    while True:
        n = int(input("What's x?? "))
        if n > 0:
            break
    return n

def meow(x):
    for _ in range(x):
        print("meow")

main()