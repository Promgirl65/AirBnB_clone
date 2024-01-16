#!/usr/bin/python3

"""
To nitialize package and retrieves storage
"""

from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
