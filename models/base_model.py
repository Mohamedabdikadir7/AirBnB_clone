from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            # If kwargs is not empty, initialize attributes from dictionary
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert strings to datetime objects
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    # Ignore __class__ key
                    setattr(self, key, value)
        else:
            # If kwargs is empty, create new instance
            self.id = str(uuid4())  # Assign a unique UUID as a string
            self.created_at = datetime.now()  # Assign current datetime
            self.updated_at = datetime.now()  # Assign current datetime

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

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
