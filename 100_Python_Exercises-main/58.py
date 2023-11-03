import json
from pprint import pprint

my_dict = {"firstName": "om", "lastName": "Priya"}

with open("json.txt", "+r") as file:
    file_data = json.load(file)
    file_data["employees"].append(my_dict)
    pprint(file_data["employees"])
