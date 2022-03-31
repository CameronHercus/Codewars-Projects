"""
6 kyu - Simple Encryption #1 - Alternating Split
"""


def encrypt(text, n):
    """6 kyu - Simple Encryption #1 - Alternating Split"""
    blank = [[], []]
    for j in range(n):
        for i in range(len(text)):
            blank[i%2].append(text[i])
        text =  "".join(blank[1]) + "".join(blank[0]) 
        blank = [[], []]
    return text


def decrypt(encrypted_text, n):
    return None
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))