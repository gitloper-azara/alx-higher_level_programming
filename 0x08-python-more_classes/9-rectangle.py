#!/usr/bin/python3
"""
A rectangle class
"""


class Rectangle:
    """A Rectangle class that defines a rectangle.
    Attributes:
        number_of_instances (int): initialised to 0, checks number of
        rectangle instances during instantiation and after deletion
        print_symbol (any type): initialised to '#', used as a symbol for
        string representation and can be any type
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Creates an instance of the rectangle class
        Args:
            width (int): an integer that stores our width value
            height (int): an int that stores our height value
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width: private instance that retrieves width value
        Args:
            width (int): int that stores width value retrieved
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width: property setter for width
        Args:
            value: sets value of width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width < 0
        """
        # handle TypeError
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """height: private instance that retrieves height value
        Args:
            height (int): int that stores height value retrieved
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height: property setter for height
        Args:
            value: sets value of height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0
        """
        # handle TypeError
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """Returns a string representation of '#' rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        else:
            rectangle_str = ''
            for _ in range(self.height):
                rectangle_str += str(self.print_symbol) * self.width + '\n'
            # remove trailing newline for last line
            return rectangle_str[:-1]

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """Prints 'Bye rectangle' on instance deletion detection"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area value."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle instance with square-like dimensions
        Args:
            size (int): size of square Rectangle dimensions
        Returns:
            new Rectangle instance with width == height == size
        """
        return cls(size, size)
