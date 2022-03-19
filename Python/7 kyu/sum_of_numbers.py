"""
7 kyu - Beginner Series #3 Sum of Numbers
"""

def get_sum(a,b):
    """7 kyu - Beginner Series #3 Sum of Numbers"""
    return sum(range(min(a, b), max(a,b)+1))

print(get_sum(3,-1))
print(get_sum(0, 2))