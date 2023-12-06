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

    def do_create(self, line):
        """
        command that creates a user infomation
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.Classes()[line]():
            print("** class doesn't exist **")
        else:
            s = storage.classes()[line]()
            s.save()
            print(s.id)

    def do_show(self, line):
        """
        command that shows the input
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            letters = line.split(' ')
            if letter[0] not in storage,classes()[line]():
                print("** class doesn't exist ***")
            elif len(letters) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], letters[1])
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
            if letters[0] not in storage.classes():
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
            if letters[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                l = [str(obj) for key, obj in storage.all().item()
                    if type(obj).__name__ == word[0]]
                print(l)
        else:
            fresh_list = [str(obj) for key, obj in storage.all().item()]
            print(fresh_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
