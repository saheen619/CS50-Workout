"""
import csv

name = input("Whats your name? ")
home = input("Where's your home? ")

with open("student_details.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""





# To write the file using a DictWriter method from csv module, to make it more dynamic

import csv

name = input("Whats your name? ")
home = input("Where's your home? ")

with open("student_details.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames = ["name","home"])
    writer.writerow({"name": name, "home": home})