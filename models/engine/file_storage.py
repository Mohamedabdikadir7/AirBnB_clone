#!/usr/bin/python3
"""
file_storage.py module
"""

import json


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
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to objects
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            # let us open the json file.
            file = FileStorage.filepath
            with open(file, encoding='utf-8') as f:
                dict1 = json.load(f)

            # now lets focus on the values of this dictionary only;
            # these values are dictionaries of instance attributes.

            for value in dict1.values():
                # extract classname to recreate our object with new method.

                name = value["class"]

                # we cannot create objects using the class name as a string
                # We need to convert it to an object using eval
                name = eval(name)

                # delete the class key because our objects dont have it

                del value["_class"]
                # recreate our objects using new
                self.new(name(**value))
        except FileNotFoundError:
            pass
