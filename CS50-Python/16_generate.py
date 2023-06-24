"""
import random

coin = random.choice(["heads","tails"])
print(coin)
"""


# importing only the required modules
"""
from random import choice

print(choice(["heads","tails"]))
"""

"""
import random

number = random.randint(1, 10)
print(number)
"""



# random.shuffle

import random

family = ["saheen","hizana","farzeen","fathima","anwar"]
random.shuffle(family)

for member in family:
    print (member)