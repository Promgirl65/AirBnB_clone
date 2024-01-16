#!/usr/bin/python3
"""This module defines the Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class represnets the Review Model"""

    place_id = ""
    user_id = ""
    text = ""
