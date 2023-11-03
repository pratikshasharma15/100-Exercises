from datetime import datetime

today = datetime.now()

year = today.strftime("%Y")
month = today.strftime("%B")
day = today.strftime("%d")
weekday = today.strftime("%A")

template = f"Today is {weekday}, {month} {day}, {year}"
print(template)

print(datetime.now().strftime("Today is %A, %B %d, %Y"))
