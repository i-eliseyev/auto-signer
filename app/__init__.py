from flask import Flask

from config import Config

def create_app():
    config = Config()
    app = Flask(__name__)
    app.config.from_object(config)
    return app

from app import routes