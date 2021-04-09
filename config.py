import os
from dotenv import load_dotenv
from flask import url_for

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Configure database variables for connection
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youwillneverknowme'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')  or \
            'mysql + pymysql://<KennedyUdeze>:<Thastreet64>@<database-1.cwvtromjtobl.us-east-2.rds.amazonaws.com>/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False