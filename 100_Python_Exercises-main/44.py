import string

with open("alphabet3.txt", "w") as file:
    for i, j, k in zip(
        string.ascii_lowercase[0::3],
        string.ascii_lowercase[1::3],
        string.ascii_lowercase[2::3],
    ):
        file.write(i + j + k)
        file.write("\n")
