#!/usr/bin/python3
"""
A function that prints 'My name is <first name> <last name>'.
"""


def say_my_name(first_name, last_name=""):
    """Say my name function definition begins.

    Args:
        first_name (str): string for first name
        last_name (str): string for last name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print(f'My name is {first_name} {last_name}')
