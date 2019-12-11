#!/usr/bin/python3
for k in range(0, 10):
    for c in range(0, 10):
        if c > k:
            print("{}{}{en}".format(k, c, en=", " if k != 8 else "\n"), end="")
