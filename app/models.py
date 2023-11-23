"""
Module for defining the User model and SQLAlchemy setup.

Classes:
- User: Represents user data with attributes id, username, and email.

Attributes:
- db: An instance of the SQLAlchemy class for database management.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    User model class for representing user data.

    Attributes:
    - id (int): Primary key for the User model.
    - username (str): User's username, unique and cannot be null.
    - email (str): User's email address, unique and cannot be null.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'

    def save_to_db(self):
        """Save the user to the database."""
        db.session.add(self)
        db.session.commit()
        db.session.close()

    @classmethod
    def find_by_username(cls, username):
        """Find a user by their username."""
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        """Find a user by their email."""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, user_id):
        """Find a user by their ID."""
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def find_all(cls):
        """Find all users."""
        return cls.query.all()

    @classmethod
    def delete_all(cls):
        """Delete all users."""
        db.session.delete(cls)
        db.session.commit()
        db.session.close()

    @classmethod
    def delete_by_id(cls, user_id):
        """Delete a user by their ID."""
        cls.query.filter_by(id=user_id).delete()
        db.session.commit()
        db.session.close()

    @classmethod
    def delete_by_username(cls, username):
        """Delete a user by their username."""
        cls.query.filter_by(username=username).delete()
        db.session.commit()
        db.session.close()

    @classmethod
    def delete_by_email(cls, email):
        """Delete a user by their email."""
        cls.query.filter_by(email=email).delete()
        db.session.commit()
        db.session.close()
