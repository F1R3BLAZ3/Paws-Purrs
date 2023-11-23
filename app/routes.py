"""Module for defining general routes."""

from flask import jsonify
from app.models import User
from app import db_storage
from . import app


@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve a list of users and return it as a JSON response.

    Returns:
    - JSON response containing a list of users with their id, username, and email.
    """
    users = db_storage.all(User)
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(user_list)
