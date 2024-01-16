#!/usr/bin/python3
"""This module defines the Class City BaseModel"""
from models.base_model import BaseModel

class City(BaseModel):
    """This represents City with a name and state ID"""

    state_id = ""
    name = ""
