#!/usr/bin/env python3
"""
This module is entry point for command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import re


class HBNBCommand(cmd.Cmd):
    """This is the class"""

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

    def default(self, _cmd):
        """
        a follow-come method that is called when a command line inout is
        not recogined, this method willbe overriden by the following lines
        of code, so that eh consile may capture commands that looks like
        User.mathod()
        """

        temp_1 = _cmd.split(".")
        tmp = storage.all()

        if len(temp_1) < 2:
            return

        temp_2 = temp_1[1].strip(")")
        temp = temp_2.strip("(")
        hold = temp_1[0]

        if temp == "all":
            return self.do_all(hold)
        elif temp == "count":
            _count = 0
            for key in tmp.keys():
                key_1 = key.split(".")
                print(key_1)
                if key_1[0] == hold:
                    _count += 1
            print(_count)

        cmd_pattern = re.compile(r'show\("([^"]*)"\)|show\(\)')
        reg = cmd_pattern.match(temp)
        print(reg)
        if temp == cmd_pattern:
            print(temp)
            for key in tmp.keys():
                key_1 = key.split(".")
                if key_1[1] == hold:
                    print()

    def do_create(self, _cmd):
        """
        command that creates a user infomation
        """
        temp = storage.existed_classes()

        if _cmd == "" or _cmd is None:
            print("** class name missing **")
            return
        if _cmd not in temp.keys():
            print("** class doesn't exist **")
            return

        new_obj = temp[_cmd]()
        new_obj.save()
        """new_obj.save(self)"""
        print(new_obj.id)
        """print(new_obj.__class__.__name__)"""

    def do_show(self, _cmd):
        """
        command that shows the input
        """
        if _cmd == "" or _cmd is None:
            print("** class name missing **")
        else:
            temp = _cmd.split(" ")
            hold = storage.existed_classes()
            if temp[0] not in hold.keys():
                print("** class doesn't exist ***")
            elif len(_cmd) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(temp[0], temp[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, _cmd):
        """
        command that deletes items
        """
        if _cmd == "" or _cmd is None:
            print("** class name missing **")
        else:
            temp = _cmd.split(" ")
            hold = storage.existed_classes()
            if temp[0] not in hold.keys():
                print("** class doesn't exist **")
            elif len(temp) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(temp[0], temp[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, _cmd):
        """
        command for all instance
        """
        if _cmd != "":
            temp = _cmd.split(" ")
            hold = storage.existed_classes()
            if temp[0] not in hold.keys():
                print("** class doesn't exist **")
            else:
                list_ = [
                    str(obj)
                    for key, obj in storage.all().items()
                    if type(obj).__name__ == temp[0]
                ]
                print(list_)
        else:
            list_2 = [str(obj) for key, obj in storage.all().items()]
            print(list_2)

    def do_count(self, _cmd):
        """
        command that counts the instance
        """
        temp = _cmd.split(" ")
        hold = storage.existed_classes()
        if not temp[0]:
            print("** class name missing **")
        elif temp[0] not in hold.keys():
            print("** class doesn't exist **")
        else:
            count_ = [_ for _ in storage.all() if a.startswith(temp[0] + ".")]
            print(len(count_))

    def do_update(self, _cmd):
        """
        command that will update and updating attribute
        """
        temp = _cmd.split(" ")
        hold = storage.existed_classes()
        tmp = storage.all()

        if not temp:
            print("** class name is missing **")
        elif temp[0] not in hold.keys():
            print("** class doesn't exist **")
        elif len(temp) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(temp[0], temp[1])
            if key not in tmp.keys():
                print("** no instance found **")
            elif len(temp) < 3:
                print("** attribute name missing **")
            elif len(temp) < 4:
                print("** value missing **")
            else:
                for _id in tmp.keys():
                    if _id == key:
                        setattr(tmp[key], temp[2], temp[3])
                        storage.save()
        print(tmp[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
