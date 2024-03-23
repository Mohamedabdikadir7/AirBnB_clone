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
        """ retrieves data again """

        try:
            with open(self.__file_path, "r") as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    module = __import__
                    ('models.' + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
