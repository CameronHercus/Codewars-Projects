"""
6 - kyu Array.diff

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
result.
It should remove all values from list a, which are present in list b keeping their order.
"""


def array_diff(a, b):
    a_copy = a
    for i in b:
        a_copy[:] = [x for x in a_copy if i != x]
    return a_copy


print(array_diff([1, 2, 2, 2, 3], [2]))
