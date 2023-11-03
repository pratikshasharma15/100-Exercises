d = {"a": list(range(1, 11)), "b": list(range(11, 21)), "c": list(range(21, 31))}

for k, v in d.items():
    template = f"'{k}': {v},\n"
    print(template)

# Note there is an inbuilt module pprint
from pprint import pprint

pprint(d)
