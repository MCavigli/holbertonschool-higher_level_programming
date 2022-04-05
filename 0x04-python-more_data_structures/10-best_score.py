#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    vals = list(a_dictionary.items())
    vals.sort()
    return vals[-1][0]
