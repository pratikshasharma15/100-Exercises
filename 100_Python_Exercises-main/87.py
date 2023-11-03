checklist = ["Portugal", "Germany", "Spain"]

with open("countries_missing.txt", "r") as file:
    contents = file.read().split("\n")

contents = contents + checklist
contents.sort()

with open("done_countries.txt", "w") as file:
    for country in contents:
        file.write(country + "\n")
