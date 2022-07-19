from flask import Flask
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS = True,
        SECRET_KEY = '063b5d59f24fbf66d126cfb5e661902f',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    )

    return app


app = create_app()
proxied = FlaskBehindProxy(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from flasksite import routes

