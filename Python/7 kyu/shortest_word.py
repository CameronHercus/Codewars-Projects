"""
7 kyu - Shortest word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    string_list = s.split(" ")
    min_length = len(string_list[0])
    for i in range(1, len(string_list), 1):
        if len(string_list[i]) < min_length:
            min_length = len(string_list[i])
    return min_length




print(find_short("bitcoin take over the world maybe who knows perhaps"))
