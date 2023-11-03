a = [1, 2, 3]
b = (4, 5, 6)

for num in range(3):
    print(a[num] + b[num])

for i, j in zip(a, b):
    print(i + j)
