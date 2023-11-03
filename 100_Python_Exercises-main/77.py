from datetime import datetime

age = int(input("Enter Your Age: "))
today = int(datetime.now().strftime("%Y"))

print(today - age)
