# Import app from the app dict
from app import create_app, db

# Import the models
from app.Homepage.model import Friends
from app.Movies.model import MoviesList

# Instatiate the app instance from __init__.py in app dict 
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'Friends':Friends, 'MoviesList':MoviesList}