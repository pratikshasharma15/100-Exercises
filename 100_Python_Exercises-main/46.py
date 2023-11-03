import string

my_list = []

for char in string.ascii_lowercase:
    file_name = f"{char}.txt"
    with open(file_name, "r") as file:
        content = file.read()
        my_list.append(content)

print(my_list)
