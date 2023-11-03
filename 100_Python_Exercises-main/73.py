# update using pandas
import pandas as pd

multiply = lambda a, b: a * b
# lists = []


# with open("data_multiply.txt", "r") as file:
#     file_content = file.read().split("\n")
#     for ind, data in enumerate(file_content):
#         if ind == 0:
#             continue
#         data = data.split(",")
#         lists.append(str(multiply(int(data[0]), int(data[1]))))


# with open("output.txt", "w") as file:
#     for data in lists:
#         file.write(data + "\n")


# print(lists)

df = pd.read_csv("data_multiply.csv")
contents = df.to_string()

contents = contents.split("\n")
print(contents)

for ind, content in enumerate(contents):
    if ind == 0:
        continue
    content = content.split("  ")
    print(multiply(int(content[1]), int(content[2])))
