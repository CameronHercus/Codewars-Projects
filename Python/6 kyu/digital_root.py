"""
6 kyu -
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a
single-digit number is produced. The input will be a non-negative integer.
"""
def digital_root(n):
    #Nine Hours, Nine Persons, Nine Doors
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    return n % 9


print(digital_root(18))