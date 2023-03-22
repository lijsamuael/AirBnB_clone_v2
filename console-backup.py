#!/usr/bin/python3
""" The main console for the project """

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit  the program"""
        return True

#defines a function called _key_value_parser  that takes   a list of strings as an argument (args).
#The function's purpose is to create a dictionary from this list of strings, where each string represents a key-value pair.

    def _key_value_parser(self, args):
#defines the function and its arguments.
        """creates a dictionary from a list of strings"""
        new_dict = {}
#initializes an empty dictionary
        for arg in args:
#starts a loop that iterates over each string in the args list
            if "=" in arg:
#checks if the current string contains an equals sign ("="), which is used to separate key-value pairs.
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]

#If the string contains an equals sign
#this block of code splits the string into two parts using the split() method.
#The first part becomes the key and the second part becomes the value.

                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
#checks if the value is enclosed in double quotes
#If it is,  it removes the quotes and replaces any underscores in the value with spaces.
#If the value is not enclosed in  quotes,
# it tries to convert it to an integer using the int() function.
# If that fails, it tries to convert it to a float using the float() function.
#If both conversion attempts fail,
#the loop continues to the next string in args using the continue statemen


                new_dict[key] = value
            #
        return new_dict
#this line returns the resulting dictionary new_dict.
    def do_create(self, arg):
#defines a method called do_create within a class
        """Creates a new instance of a class"""
        args = arg.split()
#splits the string arg into a list of arguments,
#which are separated by spaces.
        if len(args) == 0:
            print("** class name missing **")
            return False
# checks if the length of the args list is zero
#If it is, the method prints an error message and returns False.

        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
#checks if the first argument in the args list corresponds to an existing class.
#If it does, the method calls another method called _key_value_parser
#This method converts the list of arguments into a dictionary of key-value pairs.
# the method uses this dictionary to create a new instance of the specified class
#and stores it in the instance variable
#If the class does not exist, the method prints an error message and returns False.

        print(instance.id)
        instance.save()
#If the class does not exist, the method prints an error message and returns False.
#then calls the save() method of the instance
#The save() method is responsible for saving the instance to a database or file system

if __name__ == '__main__':
    HBNBCommand().cmdloop()
