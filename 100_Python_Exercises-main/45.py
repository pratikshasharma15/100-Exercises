import string

for char in string.ascii_lowercase:
    file_name = f"{char}.txt"
    content = char
    with open(file_name, "w") as file:
        file.write(content)
