from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "4572"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=14)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("ID", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(100))
    email = db.Column("Email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        session["user"] = request.form["nm"]
        flash("Logged In", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In", "info")
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None

    if "user" in session:
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email Was Saved")

        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)

    flash("Not Logged In", "info")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("Logged Out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
