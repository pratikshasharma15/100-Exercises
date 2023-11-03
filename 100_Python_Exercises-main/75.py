import pandas as pd
import matplotlib.pyplot as plt

frames = pd.read_csv("data_multiply.csv")
x = []
y = []
contents = frames.to_string().split("\n")
for _, content in enumerate(contents):
    if _ == 0:
        continue
    content = content.split("  ")
    x.append(int(content[1]))
    y.append(int(content[2]))

plt.scatter(x, y)
plt.show()

# Instructor answer
'''
data = pd.read_csv("https://www.pythonhow.com/data/sampledata.txt")
data.plot(x="x", y="y", kind="scatter")
plt.show()
'''
