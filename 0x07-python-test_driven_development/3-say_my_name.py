#!/usr/bin/python3
"""say_my_name is a function that prints names given"""


def say_my_name(first_name, last_name=""):
    """first name and last name to be printed"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
