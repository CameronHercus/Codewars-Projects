"""
7 kyu - Is this a triangle?
"""


def is_triangle(a, b, c):
    """7 kyu - Is this a triangle?"""
    sorted_list = sorted([a, b, c])
    return sorted_list[0] + sorted_list[1] > sorted_list[2]
