"""
6 kyu - Delete occurrences of an element if it occurs more than n times
"""


def delete_nth(order,max_e):
    """6 kyu - Delete occurrences of an element if it occurs more than n times"""
    blank = []
    for i in order:
        if blank.count(i) < max_e:
            blank.append(i)
    return blank


print(delete_nth([20,37,20,21], 1))