"""
This module initializes a Flask application with SQLAlchemy and CSRF protection.
"""

import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
# from flask_babel import Babel

load_dotenv()

app = Flask(__name__)

# Explicitly set the time zone
# app.config['BABEL_DEFAULT_LOCALE'] = 'en_US'  # Use your desired locale
# app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'  # Use your desired time zone

# Configuration variables
app.config['DOG_API_BASE_URL'] = 'https://api.thedogapi.com/v1'
app.config['DOG_API_KEY'] = os.getenv('DOG_API_KEY')
app.config['CAT_API_KEY'] = os.getenv('CAT_API_KEY')
app.config['CAT_API_BASE_URL'] = 'https://api.thecatapi.com/v1'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

csrf = CSRFProtect(app)

from app import dog_routes, cat_routes, models
