#import re

#email = input("What's your email address? ").strip()

#if re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
#    print("Valid")
#else:
#    print("Invalid")




""" import re

email = input("What's your email address? ").strip()

if re.search(r"^[a-z0-9_\.]+@[a-z]+\..+[\.]*[^@\.]$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid") """



import re

email = input("What's your email address? ").strip()

if re.search(r"^[a-z0-9_\.]+@(\w+\.)?[a-z]+\.[a-z]+$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
