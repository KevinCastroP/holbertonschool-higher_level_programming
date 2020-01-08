#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division = 0
        division = (a/b)
        return division
    except:
        division = None
    finally:
        print("Inside result: {}".format(division))
