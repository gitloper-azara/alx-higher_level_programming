#!/usr/bin/python3


class Square:
    """An empty class Square that defines a square."""
    def __init__(self, size) -> None:
        """Creates an instance of the Square class.

        Args:
            size (int): private instance attr of Square.

        """
        self.__size = size

    def __str__(self) -> str:
        """Returns a string representation of the Square object."""
        return "Square class instance"
