#!/usr/bin/python3
for c in range(0, 100):
    print("{:0>2d}{per}".format(c, per=", " if c < 99 else "\n"), end='')
