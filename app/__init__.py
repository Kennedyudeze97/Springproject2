# This serve as the entry point of the backend, it makes a blueprint for our application.
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# Initialize the database instance
db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    app.app_context().push()

    from app.Homepage import home_bp
    app.register_blueprint(home_bp)

    from app.Movies import movies_bp
    app.register_blueprint(movies_bp)

    return app