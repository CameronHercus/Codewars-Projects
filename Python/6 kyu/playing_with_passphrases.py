"""
6 kyu - Playing with passphrases
"""
import string
def play_pass(s, n):
    """6 kyu - Playing with passphrases"""
    lower_list = string.ascii_lowercase
    upper_list = string.ascii_uppercase
    final = []
    for i, j in enumerate(list(s)):
        if j.isalpha() is True:
            if i % 2 == 1:
                final.append(lower_list[(lower_list.index(j.lower()) + n) % 26])
            else:
                final.append(upper_list[(upper_list.index(j.upper()) + n) % 26])
        elif j.isdigit():
            final.append(str(complement(int(j))))
        else:
            final.append(j)
    return "".join(reversed(final))


def complement(number):
    for i in range(9):
        if i + number == 9:
            return i
    return 9

    
print(play_pass("xy", 1))

print(complement(9))
print(complement(7))
print(complement(0))