"""
import sys

print("Hello, my name is", sys.argv[1]) 
# In the above line of code, the index 0 for sys.argv is the name of the program.
"""




# If the user havent mentioned any command line argument while runbning the py program, it will show an IndexError
"""
import sys

try:
    print("Hello, My name is", sys.argv[1])
except IndexError:
    print("Not enough arguments. Type in your first name to continue.")
"""





# Another approach
"""
import sys

if len(sys.argv) < 2:
    print("Not enough arguments. Type in your first name to continue.")
elif len(sys.argv) > 2:
    print("Too many arguments. Type in just your first name to continue.")
else:
    print("Hello, My name is", sys.argv[1])
"""




# USing sys.exit() to exit the program

import sys

if len(sys.argv) < 2:
    sys.exit("Not enough arguments. Type in your first name to continue.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments. Type in just your first name to continue.")

print("Hello, My name is", sys.argv[1])