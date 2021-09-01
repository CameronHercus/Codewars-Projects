"""
7 kyu - Isograms

An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string 
that contains only letters is an isogram. Assume the empty string is an 
isogram. Ignore letter case.
"""

def is_isogram(string):
    blank = set()
    for i in string:
        if i.lower() in blank:
            return False
        blank.add(i.lower())
    return True

print(is_isogram("Dermatoglyphics" ))
print(is_isogram("aba" ))
print(is_isogram("moOse" ))