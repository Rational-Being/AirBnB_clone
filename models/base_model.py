#!/usr/bin/env python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes for other class
    """

    def __init__(self, *args, **kwargs):
        """This constructor takes the *args and **kwargs argument
        *args is not to be used
        """
        if len(args) > 0:
            pass

        if kwargs is not None and kwargs != dict():
            for key, value in kwargs.items():
                if key in ["created_at", "updted_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "id":
                    self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        This method is called when an object is to be orinted
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        This updates the public instance updted_At
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        A serialiazation/deserialization process that returns a dictionary
        containing all key/values of __dict__ of the instance
        """
        inst_dict = self.__dict__.copy()  # instance dictionary is stored here
        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()
        return inst_dict
