import string

my_list = []
my_string = "python"

for char in string.ascii_lowercase:
    file_name = f"{char}.txt"
    with open(file_name, "r") as file:
        content = file.read()
        if content.strip() in my_string:
            my_list.append(content)

print(my_list)
