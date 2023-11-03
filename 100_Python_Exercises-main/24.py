d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

for k, v in d.items():
    template = f"{k} has value {v}"
    print(template)
