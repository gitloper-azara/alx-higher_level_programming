#!/usr/bin/python3
"""
A function that prints text with 2 new lines after each of these characters:
'.', '?', and ':'
"""


def text_indentation(text):
    """function definition for text_indentation().

    Args:
        text (str): input string to use
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    punctuation_set = {'.', '?', ':'}
    current_line = ''

    for idx, char in enumerate(text):
        current_line += char
        if char in punctuation_set:
            # check if there is another character after the current one
            if idx + 1 < len(text):
                print(current_line.strip())
                # print two new lines
                print()
                current_line = ''

    if current_line:
        print(current_line.strip(), end='')
