#!/usr/bin/python3
def search_replace(my_list, search, replace):
    KC = my_list[:]
    for prev_value, new_value in enumerate(KC):
        if new_value == search:
            KC[prev_value] = replace
    return (KC)
