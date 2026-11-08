import os
from flask_migrate import Migrate

from src.app import create_app, db


# This file is used to make database migrations simpler

env_name = os.getenv("FLASK_ENV")
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

# flask-script is unmaintained and incompatible with current Flask; the "db"
# commands are now provided by the Flask CLI: flask --app manage db <command>
