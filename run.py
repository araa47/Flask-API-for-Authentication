# /run.py
import os

# import to load environment variables
from dotenv import load_dotenv, find_dotenv

# import flask create app from project
from src.app import create_app

# load env vars
load_dotenv(find_dotenv())

# get the env name development/production/testing
env_name = os.getenv("FLASK_ENV")

app = create_app(env_name)

# Run app on corresponding port
if __name__ == "__main__":
    port = os.getenv("PORT")
    # run app
    app.run(host="0.0.0.0", port=port)
