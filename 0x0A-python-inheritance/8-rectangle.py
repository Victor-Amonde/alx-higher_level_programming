#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    '''class BaseGeometry'''
    def area(self):
        '''method for getting area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''method integer validator'''
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("<name> must be an integer")
        elif self.value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value


class Rectangle(BaseGeometry):
    '''a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
