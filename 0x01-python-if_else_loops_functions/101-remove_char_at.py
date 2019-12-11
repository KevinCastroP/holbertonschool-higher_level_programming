#!/usr/bin/python3
def remove_char_at(str, n):
    res_arr = []
    for pos, char in enumerate(str):
        if pos is not n:
            res_arr.append(char)
    return "".join(res_arr)
