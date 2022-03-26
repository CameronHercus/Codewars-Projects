"""
6 kyu - Sum of Digits/Digital Root 
"""


def digital_root(n):
    """6 kyu - Sum of Digits/Digital Root"""
    digit_sum = sum([int(i) for i in str(n)])
    while digit_sum > 9:
        digit_sum = sum([int(j) for j in str(digit_sum)])
    return digit_sum
print(digital_root(16))