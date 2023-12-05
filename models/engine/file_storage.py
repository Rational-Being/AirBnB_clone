#!/usr/bin/env python3

class FileStorage():
    """
    this class serialize insatnace to Json
    and deserializes Json to instance
    """

    __file.path = file.json
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{} {}".format(obj.__name__, str(obj.id))
        FileStorage.__objects[key] = obj
