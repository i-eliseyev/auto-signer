from flask import Flask

from config import Config

app = Flask(__name__)
def create_app():
    config = Config()
    app.config.from_object(config)
    return app

from app import routes