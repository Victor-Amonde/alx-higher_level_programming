#!/usr/bin/python3
'''class Rectangle that defines rectangle'''


class Rectangle:
    '''initialization of the class'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    '''private instance attribute: width'''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    '''private instance attribute: height'''
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''returns rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns rectangle perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)