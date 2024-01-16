#!/usr/bin/python3
"""This module defines the Class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class Represents the User with
    Attributes:
        email (str): the user email
        password (str): the user password
        first_name (str): first name of user
        last_name (str): last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
