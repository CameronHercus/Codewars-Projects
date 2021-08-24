import re

"""
5 kyu - String incrementer

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(str1):
    digits = re.findall(r'\d+', str1)
    if digits:
        og_number = digits[-1]
        str1 = str1.rsplit(og_number, 1)[0]
        new_number = str(int(og_number) + 1)
        return str1 + "0" * (len(og_number) - len(new_number)) + new_number
    else:
        return str1 + "1"
