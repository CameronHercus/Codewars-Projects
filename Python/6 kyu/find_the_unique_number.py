"""
6 kyu - Find the unique number
"""

def find_uniq(arr):
    """6 kyu - Find the unique number"""
    if arr[0:3].count(arr[0]) >= 2:
        prev = arr[0]
        for i in arr[1:]:
            if prev != i:
                return i
    return arr[0]


print(find_uniq([ 3, 10, 3, 3, 3 ]))