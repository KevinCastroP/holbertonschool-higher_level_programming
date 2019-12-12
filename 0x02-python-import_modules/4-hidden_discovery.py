#!/usr/bin/python3
import hidden_4


def main():
    for kc in dir(hidden_4):
        if str(kc)[0] != "_":
            print(kc)


if __name__ == '__main__':
    main()
