#!/usr/bin/python3
"""
file_storage.py module
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ A class used for data storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ lists available objects """

        return self.__objects

    def new(self, obj):
        """ adds new objects to the list"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ saves the data """
        all_objs = self.__objects
        serialized_objects = {}
        for obj_key, obj_value in all_objs.items():
            key = "{}.{}".format(obj_value.__class__.__name__, obj_value.id)
            serialized_objects[key] = obj_value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)


    def reload(self):
        """ retrieves data again """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    serialized_objects = json.load(f)
                    for key, value in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**values)
                        self.__objects[key] = instance
                except Exception:
                    pass
