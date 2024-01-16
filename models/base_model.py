#!/usr/bin/python3
"""This script defines the Class BaseModel"""

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """This represents the parent Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """This initializethe Parent Class
        Args:
            *args: Arguments List
            **kwargs: Key/Value Attributes
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at : with Current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns the dictionary with key/values
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Returns the __str__ representation"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
