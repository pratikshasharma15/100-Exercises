user_input = input("Enter the values: ").strip()

user_input = user_input.split(",")

with open("csv_output.txt", "w") as file:
    for data in user_input:
        file.write(data + "\n")
