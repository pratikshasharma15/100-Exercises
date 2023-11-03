d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"},
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"},
    ],
}

new_dict = {"firstName": "Albert", "lastName": "Bert"}
d["employees"].append(new_dict)

print(d)
