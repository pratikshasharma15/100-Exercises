from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

user_data = {}


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


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]

        # checking for existing user
        for value in user_data.values():
            if value["username"] == username:
                return "User Already Exists"

        password = request.form["password"]

        # checking for password
        if (
            not len_checker(password)
            or not numeric_check(password)
            or not upper_check(password)
        ):
            return "Invalid Password Format"

        # proceed with saving

        index = len(user_data)
        user_data[index] = {"username": username, "password": password}
        print(user_data)
        return redirect("/")
    return render_template("home.jinja2")


if __name__ == "__main__":
    app.run(debug=True)
