#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = set(my_list)
    _sum = 0
    for count in copy_list:
        _sum += count
    return (_sum)
