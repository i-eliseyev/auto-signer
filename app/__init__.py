from flask import Flask

from config import Config

app = Flask(__name__)
config = Config()
app.config.from_object(config)

from . import routes