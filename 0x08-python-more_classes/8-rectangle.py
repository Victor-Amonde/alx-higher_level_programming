#!/usr/bin/python3
'''class Rectangle that defines rectangle'''


class Rectangle:
    '''initialization of the class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

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

    def __str__(self):
        '''print definition'''
        str_r = ""
        if self.__height == 0 or self.__width == 0:
            return str_r

        rec = []
        for i in range(self.__height):
            [rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        '''return a string representation of the rectangle to
        be able to recreate a new instance by using eval()'''
        rep = "Rectangle({}, {})".format(self.__width, self.__height)
        return rep

    def __del__(self):
        '''instance deletion detection'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
