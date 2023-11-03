user_input = input("Enter the Value: ")

lis = []
while user_input != "SAVE" or user_input != "CLOSE":
    lis.append(user_input)

    user_input = input("Enter the Value: ")
    if user_input == "SAVE" or user_input == "CLOSE":
        lis.append(user_input)
        break

last_index = len(lis) - 1

if len(lis) == 0:
    print("Nothing Happend")
elif lis[last_index] == "SAVE":
    lis.remove("SAVE")
    with open("output_97.txt", "a") as file:
        for data in lis:
            file.write(data + "\n")
else:
    print("You Just Cancel Your request")
