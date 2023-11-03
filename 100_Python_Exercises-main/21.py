d = {"a": 1, "b": 2, "c": 3}
my_dict = {k: v for k, v in d.items() if v <= 1}
print(my_dict)
