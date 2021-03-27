from flask import Blueprint

movies_bp = Blueprint('movies', __name__, template_folder='templates')

from app.Movies import routes