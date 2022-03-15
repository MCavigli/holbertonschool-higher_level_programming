#!/usr/bin/python3


def no_c(my_string):
    idx = 0
    new_list = []
    new_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            new_list.append(i)
    new_string = new_string.join(new_list)
    return new_string
