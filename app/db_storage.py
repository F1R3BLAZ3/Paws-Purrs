"""
Module for defining a SQLAlchemy-based storage class.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DBStorage:
    """A simple SQLAlchemy-based storage class."""

    def __init__(self, app_instance):
        """
        Initialize the DBStorage instance.

        Parameters:
        - app_instance: Flask application instance
        """
        self.app_instance = app_instance
        self.init_app()

    def init_app(self):
        """Initialize the app_instance with the database."""
        db.init_app(self.app_instance)

    def all(self, cls=None):
        """
        Retrieve all objects of a given class or all objects if no class is specified.

        Parameters:
        - cls: Class (optional)

        Returns:
        - List of objects
        """
        if cls is None:
            return db.session.query(cls).all()
        return db.session.query(cls).all()

    def new(self, obj):
        """
        Add a new object to the session and commit the changes.

        Parameters:
        - obj: Object to be added
        """
        db.session.add(obj)
        db.session.commit()

    def delete(self, obj):
        """
        Delete an object from the session and commit the changes.

        Parameters:
        - obj: Object to be deleted
        """
        db.session.delete(obj)
        db.session.commit()

    def update(self):
        """
        Update objects in the session and commit the changes.
        """
        db.session.commit()

    def save(self):
        """Commit changes to the session."""
        db.session.commit()

    def close(self):
        """Close the session."""
        db.session.close()
