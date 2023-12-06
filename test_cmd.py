#!/usr/bin/env python3
"""
This module is entry point for command interpreter
"""

import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.engine.file_storage import FileStorage



class HBNBCommand(cmd.Cmd):
    """ This is the class """

    prompt = "(hbnb) "

    def default(self, line):
        """
        This will catch any command if it matches nothing
        """
        self._precmd(line)

    def do_EOF(self, line):
        """
        command that exits the console
        """
        print()
        return True

    def do_quit(self, line):
        """
        command to quit a program
        """
        print("quitting program...")
        return True

    def emptyline(self, line):
        """
        will do nothing
        """
        pass

    def do_create(self, _cmd):
        """
        command that creates a user infomation
        """
        temp = storage.classes()

        if _cmd == "" or _cmd is None:
            print("** class name missing **")
            return

        if _cmd not in temp.keys():
            print("** class doesn't exist **")
            return

        new_obj = temp[_cmd]()
        new_obj.save()
        #new_obj.save(self)
        print(new_obj.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
