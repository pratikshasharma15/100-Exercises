with open("alphabet.txt", "w") as file:
    for num in range(26):
        file.write(chr(ord("a") + num))
        file.write("\n")
