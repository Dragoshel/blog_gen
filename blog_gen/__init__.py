from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
app.config.from_prefixed_env()


db = SQLAlchemy()
db.init_app(app)

from . import handlers