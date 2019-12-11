#!/usr/bin/python3
up = False
for kc in reversed(range(97, 123)):
    if up is False:
        up = True
    else:
        kc = kc - 32
        up = False
    print("{:c}".format(kc), end='')
