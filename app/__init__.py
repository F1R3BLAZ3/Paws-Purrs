"""
This module initializes a Flask application with SQLAlchemy and CSRF protection.
"""

import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from app.db_storage import DBStorage

app = Flask(__name__)

from app import dog_routes, models

load_dotenv()

csrf = CSRFProtect(app)
db_storage = DBStorage(app)

username = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PWD')
host = os.getenv('MYSQL_HOST')
dbname = os.getenv('MYSQL_DB')

# Configuration variables
app.config['DOG_API_BASE_URL'] = 'https://api.thedogapi.com/v1'
app.config['DOG_API_KEY'] = os.getenv('DOG_API_KEY')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{host}/{dbname}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
