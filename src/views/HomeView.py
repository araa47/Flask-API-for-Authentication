from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserSchema
from ..shared.Authentication import Auth
from flask import render_template
from flask import request, json, Response, Blueprint, g


website_api = Blueprint("website_api", __name__)
user_schema = UserSchema()


@website_api.route("/login.html", methods=["GET"])
def return_login():
    return render_template("login.html")


@website_api.route("/stats.html", methods=["GET"])
def return_stats():
    return render_template("stats.html")


@website_api.route("/signup.html", methods=["GET"])
def return_signup():
    return render_template("signup.html")
