from flask import Flask
from views import library
from config import DevConfig, Config
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.config.from_object(Config)
    app.register_blueprint(library)
    db=SQLAlchemy(app)
    return app
