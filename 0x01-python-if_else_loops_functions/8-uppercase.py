#!/usr/bin/python3


def uppercase(str):
    for i in str:
        tmp = ord(i)
        if tmp >= 97 and tmp <= 122:
            pr = chr(tmp - 32)
        else:
            pr = i
        print('{}'.format(pr), end="")
    print()
