#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self):
        """Initialize a new BaseModel."""
        self.id = str(uuid4())  # Assign a unique UUID as a string
        self.created_at = datetime.now()  # Assign current datetime
        self.updated_at = datetime.now()  # Assign current datetime

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()  # Update updated_at with current datetime

    def to_dict(self):
        """Return a dictionary containing all instance attributes."""
        obj_dict = self.__dict__.copy()  # Get a copy of instance attributes
        # Convert datetime objects to ISO format strings
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        # Add the class name to the dictionary
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,  # Class name
            self.id,  # Unique ID
            self.__dict__  # Dictionary representation of instance attributes
        )

