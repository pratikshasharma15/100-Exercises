import re


def len_checker(data):
    return len(data) >= 5


def cap_check(data):
    res = re.search("[0-9]+", data)
    if res is not None:
        return True
    return False


def upper_check(data):
    res = re.search("[A-Z]+", data)
    if res is not None:
        return True
    return False


while True:
    password = input("Enter Your Password: ")
    if len_checker(password) and cap_check(password) and upper_check(password):
        print("Ok")
        break
    else:
        print("Invalid Password")


"""
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
"""
