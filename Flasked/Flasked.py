from flask import Flask, redirect, url_for

app = Flask(__name__)

adminAccess = True


@app.route("/")
def home():
    return "Welcome To The Home <h1>This Is Home</h1>"


@app.route("/<name>")
def user(name):
    return f"Hello, {name}"


@app.route("/admin")
def admin():
    if adminAccess:
        return "Welcome Admin, What Would You Like To Change Today"

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
