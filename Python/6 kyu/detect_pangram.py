"""
6 kyu - detect pangram
"""

import string

def is_pangram(s):
    """6 kyu - detect pangram """
    alphabet_dict = dict.fromkeys(string.ascii_lowercase, False)
    for i in s:
        if i.lower() in alphabet_dict:
            alphabet_dict[i.lower()] = True
    return all(i is True for i in alphabet_dict.values())


pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram(pangram)