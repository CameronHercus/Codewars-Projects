"""
7 kyu -
Mumbling

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""


def accum(s):
    return "-".join([s[i].upper() + s[i].lower() * i for i in range(len(s))])


print(accum("abcd"))
