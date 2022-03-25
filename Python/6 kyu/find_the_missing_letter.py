"""
6 kyu - Find the missing letter
"""
import string

def find_missing_letter(chars):
    """6 kyu - Find the missing letter"""
    if chars[0].isupper():
        alphabet_string = list(string.ascii_uppercase)
    else:
        alphabet_string = list(string.ascii_lowercase)
    start_index = alphabet_string.index(chars[0])
    counter = 0
    for i in chars:
        if alphabet_string[start_index+counter] != i:
            return alphabet_string[start_index+counter]
        counter += 1
    return None

print(find_missing_letter(['O','Q','R','S']))