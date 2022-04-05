#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m = 0
    best = ''
    for k, v in a_dictionary.items():
        if v > m:
            m = v
            best = k
    return best
