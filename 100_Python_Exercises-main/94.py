with open("urls.txt", "r") as file:
    contents = file.read()

contents = contents.split("\n")
lis = []
for content in contents:
    content = content.replace("https", "http")
    lis.append(content + "\n")
print(lis)

with open("urls_output.txt", "w") as file:
    file.writelines(lis)
