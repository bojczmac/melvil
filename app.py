from flask import Flask
from views import library
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from xlsx_reader import get_book
from init_db import db
#db = SQLAlchemy()

def create_app(config=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(library)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        get_book()
    return app

create_app(DevConfig)


