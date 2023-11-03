with open("countries_raw.txt", "r") as file:
    contents = file.read().split("\n")

filtered_content = filter(lambda x: x != "" and len(x) != 1 and x != "\n", contents)

ok_country = []
for content in filtered_content:
    if content == "Top of Page":
        continue
    ok_country.append(content + "\n")

with open("best.txt", "w") as file:
    file.writelines(ok_country)
