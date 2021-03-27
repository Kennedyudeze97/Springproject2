from flask import Blueprint

home_bp = Blueprint('Home', __name__, template_folder='templates')

from app.Homepage import routes