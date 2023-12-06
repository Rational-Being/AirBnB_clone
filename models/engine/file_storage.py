#!/usr/bin/env python3

from os import path
import json

class FileStorage:
    """
    this class serialize insatnace to Json
    and deserializes Json to instance
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        creates a key i.e a unique identifier for any instance (obj) created
        using this key, create a key, value pair to the __objects attribute
        now, key = instance name dot its uuid and value = to the objects
        i.e. the neew instance i.e the new user created (obj)
        therefore, he new method populate the __objects class attribute
        """
        key = "{}.{}".format(type(obj).__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def classes(self):
        pass

    def save(self):
        """
        an empty dictionary is first created, it be se serialized to jsoon
        inside it, the key = FileStorage.__object keys value i.e instance.id
        value = the instance.to_dict() - to_dict can be found in the base model
        """
        objects_created = {}
        for key, value in FileStorage.__objects.items():
            objects_created[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as newly_created_file:
            json.dump(objects_created, newly_created_file)

    def reload(self):
        """
        reloads the stored object
        """
        if not path.isfile(FileStorage.__file_path):
            return

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Review": Review,
        }
        return classes

        try:
            with open(FileStorage.__file_path, "r") as newly_created_file:
                """
                an attempt to conert json to python strin
                therfore, json.loads is ascribed a variable
                """
                json_strings = json.load(newly_created_file)

            for key, value in json_strings.items():
                if value["__class__"] in classes.keys():
                    value = classes[key.split(".")[0]](**value)
                    FileStorage.__objects.update({key: value})
#                FileStorage.__objects[key] = BaseModel(**value)

        except Exception:
            pass

