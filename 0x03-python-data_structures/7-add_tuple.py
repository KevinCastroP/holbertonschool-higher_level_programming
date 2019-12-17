#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tk = tuple_a + (0, 0)
    tc = tuple_b + (0, 0)
    return ((tk[0] + tc[0]), (tk[1] + tc[1]))
