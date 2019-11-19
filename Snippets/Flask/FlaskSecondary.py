from flask import Blueprint, render_template

secondary = Blueprint(
    "Secondary", __name__, static_folder="static", template_folder="templates"
)


@secondary.route("/home")
@secondary.route("/")
def home():
    return render_template("index.html")
