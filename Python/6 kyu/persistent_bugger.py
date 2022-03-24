"""
6 kyu - Persistent Bugger.
"""
import math


def persistence(n):
    """6 kyu - Persistent Bugger."""
    counter = 0
    digit_list = [int(i) for i in str(n)]
    while len(digit_list) != 1:
        digit_list = list(int(i) for i in str(math.prod(digit_list)))
        counter += 1
    return counter
