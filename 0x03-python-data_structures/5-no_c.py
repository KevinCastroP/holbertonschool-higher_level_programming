#!/usr/bin/python3
def no_c(my_string):
    k = []
    for b in my_string:
        if b != 'c' and b != 'C':
            k.append(b)
    return "".join(k)
