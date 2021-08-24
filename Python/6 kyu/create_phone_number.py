"""
6 kyu - Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9), that returns
a string of those numbers in the form of a phone number.

Example:
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""


def create_phone_number(n):
    string = "".join(str(x) for x in n)

    return "(" + string[0:3] + ") " + string[3:6] + "-" + string[6:]
