#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        vals = list(a_dictionary.items())
        vals.sort()
        return vals[-1][0]
