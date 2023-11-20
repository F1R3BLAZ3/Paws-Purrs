"""
This module initializes a Flask application with SQLAlchemy and CSRF protection.
"""

import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration variables
app.config['DOG_API_BASE_URL'] = 'https://api.thedogapi.com/v1'
app.config['DOG_API_KEY'] = os.getenv('DOG_API_KEY')

csrf = CSRFProtect(app)

from app import routes, models
