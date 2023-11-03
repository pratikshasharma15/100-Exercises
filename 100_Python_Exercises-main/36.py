with open("words1.txt", "r") as file:
    file_content = file.readline()
    file_content = file_content.split(" ")
    print(len(file_content))
