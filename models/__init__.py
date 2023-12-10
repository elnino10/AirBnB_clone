#!/usr/bin/python3
"""__init__ package module"""


from .amenity import Amenity
from .base_model import BaseModel
from .city import City
from models.engine.file_storage import FileStorage
from .place import Place
from .review import Review
from .state import State
from .user import User


storage = FileStorage()
storage.reload()

all_class = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}
