"""
6 kyu - Find the odd Int
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    blank = {}
    for i in seq:
        if blank.get(i) == 1:
            blank[i] += 1
        else:
            blank[i] = 1
    for j in blank:
        if blank[j] % 2 != 0:
            return j
    return None

# Alternative solution but slower
# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))
#expected value 4