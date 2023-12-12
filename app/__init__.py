"""
This module initializes a Flask application with CSRF protection.
"""

import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

# Set the 'static' folder for serving static files
app.static_folder = 'static'

# Configuration variables for Dog and Cat APIs
app.config['DOG_API_BASE_URL'] = 'https://api.thedogapi.com/v1'
app.config['DOG_API_KEY'] = os.getenv('DOG_API_KEY')
app.config['CAT_API_BASE_URL'] = 'https://api.thecatapi.com/v1'
app.config['CAT_API_KEY'] = os.getenv('CAT_API_KEY')

# Enable pretty-printing of JSON responses
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# CSRF protection for the application
csrf = CSRFProtect(app)

# Import routes and models from the application
from app import dog_routes, cat_routes, models
