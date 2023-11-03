import json
from pprint import pprint

with open("json.txt", "r") as file:
    file_content = json.load(file)

pprint(file_content)
