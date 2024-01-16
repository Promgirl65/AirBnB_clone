#!/usr/bin/python3
"""This module defines the Class Place"""
from models.base_model import BaseModel

class Place(BaseModel):
    """This is a representation of Class Place with

    Attributes:
        The City id (str)
        The User id (str)
        The name of the place (str)
        The description of the place (str)
        The number of rooms of the place (str)
        The number of bathrooms of the place (int)
        The maximum number of guests of the place (int)
        The price by night of the place (int)
        The latitude of the place (float)
        The longitude of the place (float)
        A list of Amenity ids (list)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
