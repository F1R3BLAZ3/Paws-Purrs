"""
This module initializes a Flask application with SQLAlchemy and CSRF protection.
"""

import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Configuration variables
app.config['DOG_API_BASE_URL'] = 'https://api.thedogapi.com/v1'
app.config['DOG_API_KEY'] = os.getenv('DOG_API_KEY')

csrf = CSRFProtect(app)

print(f"DOG_API_BASE_URL: {app.config.get('DOG_API_BASE_URL')}")
print(f"DOG_API_KEY: {app.config.get('DOG_API_KEY')}")

from app import routes, models
