#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    if length == 1:
        print("0")
    elif length == 2:
        print("{}".format(sys.argv[1]))
    else:
        res = 0

        for argc in range(1, length):
            res += int(sys.argv[argc])
        print("{}".format(res))
if __name__ == '__main__':
    main()
