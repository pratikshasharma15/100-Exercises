with open("words2.txt", "r") as file:
    file_content = file.read()
    file_content = file_content.replace(",", " ").split(" ")
    print(len(file_content))
