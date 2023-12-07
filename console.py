#!/usr/bin/env python3
"""
This module is entry point for command interpreter
"""

import cmd
from models.base_model import BaseModel
import json


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
        temp = storage.existed_classes()

        if _cmd == "" or _cmd is None:
            print("** class name missing **")
            return
        if _cmd not in temp.key():
            print("** class doesn't exist **")
            return

        new_obj = temp[_cmd]()
        new_obj.save()
        """new_obj.save(self)"""
        print(new_obj.id)
        """print(new_obj.__class__.__name__)"""

    def do_show(self, line):
        """
        command that shows the input
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            letters = line.split(' ')
            if letter[0] not in storage.existed_classes()[line]():
                print("** class doesn't exist ***")
            elif len(letters) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(letters[0], letters[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        command that deletes items
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            letters = line.split(' ')
            if letters[0] not in storage.existed_classes():
                print("** class doesn't exist **")
            elif len(letters) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(letters[0], letters[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        command for all instance
        """
        if line != "":
            letters = line.split(' ')
            if letters[0] not in storage.existed_classes():
                print("** class doesn't exist **")
            else:
                le = [str(obj) for key, obj in storage.all().item()
                      if type(obj).__name__ == word[0]]
                print(le)
        else:
            fresh_list = [str(obj) for key, obj in storage.all().item()]
            print(fresh_list)

    def do_update(self, line):
        """
        command that will update and updating attribute
        """
        if line == "" or line is None:
            print("** class name missing **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
