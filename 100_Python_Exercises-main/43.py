with open("alphabet2.txt", "w") as file:
    num = 0
    while num < 26:
        file.write(chr(ord("a") + num))
        num = num + 1
        file.write(chr(ord("a") + num))
        num = num + 1
        file.write("\n")
