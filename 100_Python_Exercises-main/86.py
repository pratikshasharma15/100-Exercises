checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    contents = file.read().split("\n")

checklist = [check for check in checklist if check in contents]

print(checklist)
