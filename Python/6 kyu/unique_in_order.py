"""
6 kyu - Unique In Order

Implement the function unique_in_order which takes as argument a 
sequence and returns a list of items without any elements with the
 same value next to each other and preserving the original order 
 of elements.
"""

def unique_in_order(iterable):
    """Equal Sides Of An Array"""
    prev = None
    blank = []
    for i in iterable:
        if i != prev:
            blank.append(i)
            prev = i
    return blank


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))
