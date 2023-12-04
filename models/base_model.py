#!/usr/bin/python3
"""
base model module, for managing all objects
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String Representation of class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        temp_dict = {}
        for key, value in self.__dict__.items():
            temp_dict[key] = value if ["created_at","updated_at"].count(key) == 0\
                else self.__getattribute__(key).isoformat()
        return temp_dict