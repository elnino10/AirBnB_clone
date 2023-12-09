#!usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
import os

from models.base_model import BaseModel


class FileStorage:
    """file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(my_dict, file, indent=3)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = {
                    key: BaseModel(**val) for key, val in json.load(file).items()
                }

        # using a for loop
        # if os.path.exists(self.__file_path):
        #     with open(self.__file_path, "r", encoding="utf-8") as f:
        #         # deserialize file content
        #         json_data = json.load(f)

        #         my_obj = {}
        #         # for each key of the dict, assign an object instance to it
        #         for key, val in json_data.items():
        #             my_obj[key] = BaseModel(**val)

        #         # upadate the __objects attribbute
        #         self.__objects = my_obj
