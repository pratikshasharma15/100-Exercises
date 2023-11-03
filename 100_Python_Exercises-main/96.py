user_input = input("Enter the Value: ")

while user_input != "CLOSE":
    with open("output_96.txt", "a") as file:
        file.write(user_input + "\n")

    user_input = input("Enter the Value: ")
