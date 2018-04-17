from random import random


def most_common(lst):
    return max(set(lst), key=lst.count)

def weighted_random_by_dct(dct):
    rand_val = random()
    total = 0
    for k, v in dct.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'
    
