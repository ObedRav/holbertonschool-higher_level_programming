#!/usr/bin/python3
""" This module is about define a square """


class Square:
    """ This is a class that have size as a private property and
        run vallidations to the arguments"""
    def __init__(self, size=0):
        """ Attributes: size (int): size of the square """
        if not isinstance(size, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:  # If size is negative
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        if value < 0:  # If size is negative
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Function to calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Function to print the hash depending the value of size"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
