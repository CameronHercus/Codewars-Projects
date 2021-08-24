"""
7 kyu - Vowel Count

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""

def getCount(sentence):
    vowels_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    return len([i for i in sentence if i in vowels_set])

print(getCount("abracadabra"))