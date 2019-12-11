#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if char > 96:
            char = char - 32
        print("{:c}".format(char), end="")
    print("")
