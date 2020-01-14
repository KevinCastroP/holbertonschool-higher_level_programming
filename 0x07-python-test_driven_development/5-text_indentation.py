#!/usr/bin/python3
"""
text_indentation - printing a text divide for ".""?"
text: string to print
"""
def text_indentation(text):
    """
    Method to print a text divide
    """
    error = "text must be a string"
    count = 0
    if not (isinstance(text, str)):
        raise TypeError(error)
    while count < len(text) and text[count] == " ":
        count += 1
    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < len(text) and text[count] == " ":
                count += 1
            continue
        count += 1
