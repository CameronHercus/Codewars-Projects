"""
8 Kyu - Multiply

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    return sum([i for i in arr if i > 0])


# print(positive_sum([1,-4,7,12]))


# def positive_sum(arr):
#     """Alternative solution"""
#     total_sum = 0
#     for i in arr:
#         if i > 0:
#             total_sum += i
#     return total_sum