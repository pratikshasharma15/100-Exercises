import re


def len_checker(data):
    if len(data) >= 5:
        return True
    else:
        print("Length Must be 5 char Long")
        return False


def numeric_check(data):
    res = re.search("[0-9]+", data)
    if res is not None:
        return True
    else:
        print("Must Have numeric data")
        return False


def upper_check(data):
    res = re.search("[A-Z]+", data)
    if res is not None:
        return True
    else:
        print("Must Have Upper letter")
        return False


user_existed = True


def check(name):
    with open("users.txt", "r") as file:
        registered_users = file.read().split("\n")
        for user in registered_users:
            if user.lower() == name:
                print("User Already Exists")
                break
        else:
            print("Username is Fine!")
            return False
        return True


while user_existed:
    username = input("Enter Your Username: ").lower()
    user_existed = check(username)

# same code for password
while True:
    password = input("Enter Your Password: ")
    if len_checker(password) and numeric_check(password) and upper_check(password):
        print("Ok")
        break
    else:
        print("Invalid Password")
