from flask import Blueprint, render_template

HomeResource = Blueprint('home', __name__, url_prefix='/')


@HomeResource.route('/')
def home() -> str:
    return render_template("home.html")
