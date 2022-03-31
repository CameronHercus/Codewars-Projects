"""
6 kyu - Count characters in your string
"""

def count(string):
    """6 kyu - Count characters in your string"""
    return {i:string.count(i) for i in string}

print(count('aba'))