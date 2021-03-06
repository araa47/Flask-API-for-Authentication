# src/app.py

from flask import Flask
from flask_cors import CORS, cross_origin
from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint

from .views.HomeView import website_api as home_blueprint


def create_app(env_name):
    """
  Create app
  """

    # app initiliazation
    app = Flask(__name__)
    # enable CORS
    CORS(app)
    app.config.from_object(app_config[env_name])

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")
    app.register_blueprint(home_blueprint, url_prefix="/")

    @app.route("/", methods=["GET"])
    def index():
        """
    example endpoint
    """
        return "Welcome, please visit https://prenetics.herokuapp.com/login.html"

    return app
