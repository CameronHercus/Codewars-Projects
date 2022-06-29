"""
6 kyu - Sort the odd
"""


def sort_array(source_array):
    """Return a sorted array."""
    odd_array = [i for i in source_array if i % 2 == 1]
    odd_array.sort()
    counter = 0
    for j in range(len(source_array)):
        if source_array[j] % 2 == 1:
            source_array[j] = odd_array[counter]
            counter += 1
    return source_array

print((sort_array([5, 3, 2, 8, 1, 4])))