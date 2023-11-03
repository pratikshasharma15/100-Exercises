from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_data = {}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        index = len(user_data)
        user_data[index] = {"username": username, "password": password}
        print(user_data)
        return redirect("/")
    return render_template("home.jinja2")


if __name__ == "__main__":
    app.run(debug=True)
