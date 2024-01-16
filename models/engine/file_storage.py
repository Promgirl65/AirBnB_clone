#!/usr/bin/python3
"""This module is for the Class FileStorage."""

import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """ This is a representation of the Storage engine.

    Attributes:
        __file_path (str): name of the file to save objects in
        __objects (dict): Dictionary for the instantiated objects
        class_dict (dict): Dictionary for all classes
    """

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        Returns the Dictionary of
        <class>.<id> : object instance
        """
        return self.__objects

    def new(self, obj):
        """This sets new __objects to the original dictionary of instances."""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """This Serializes object dictionaries to the json file"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """This Deserializes existing object dictionaries to instances"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
