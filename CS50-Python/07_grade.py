"""
score = int(input("Score : "))

# Using and operator
if score >= 90 and score <= 100:
    print("Grade : A")
elif score >= 80 and score < 90:
    print("Grade : B")
elif score >= 70 and score < 80:
    print("Grade : C")
elif score >= 60 and score < 70:
    print("Grade : D")
else:
    print("Grade : F")
"""


# Better code: 
# The computer is being asked fewer quiestions, by reducing the number of boolean responses from the computer. Thus making the code efficient.

"""
score = int(input("Score : "))

if 90 <= score <= 100:
    print("Grade : A")
elif 80 <= score < 90:
    print("Grade : B")
elif 70 <= score < 80:
    print("Grade : C")
elif 60 <= score < 70:
    print("Grade : D")
else:
    print("Grade : F")
"""


# Considering the logic for the problem statement, if we know that the maximum scores can go only until 100,
# We could logically correct the code as such: 

score = int(input("Score : "))

if score >= 90:
    print("Grade : A")
elif score >= 80:
    print("Grade : B")
elif score >= 70:
    print("Grade : C")
elif score >= 60:
    print("Grade : D")
else:
    print("Grade : F")

# Thus making the code more readable, more maintainable, and efficient