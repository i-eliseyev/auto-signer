from flask import Flask

from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
config = Config()
app.config.from_object(config)
Bootstrap(app)

from . import routes