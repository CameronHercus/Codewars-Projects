"""
6 Kyu - Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
integer N. Write a method that takes the array as an argument and returns this "outlier" N.
"""


def find_outlier(integers):
    first_3 = integers[0] % 2 + integers[1] % 2 + integers[2] % 2
    if first_3 < 2:
        remainder = 1
    else:
        remainder = 0
    for i in integers:
        if i % 2 == remainder:
            return i
    return None
