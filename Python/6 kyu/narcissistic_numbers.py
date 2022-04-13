"""
6 kyu - Does my number look big in this?
"""


def narcissistic( value ):
    """6 kyu - Does my number look big in this?"""
    return sum([int(i) ** len(str(value)) for i in str(value)]) == value


narcissistic(7)
