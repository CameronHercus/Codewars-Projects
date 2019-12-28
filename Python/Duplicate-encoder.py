# O(n^2)
def duplicate_encode(word):
    str1 = ""
    for i in word.lower():
        # .count will always be O(n) so could be improved to terminate at freq at 2
        if word.lower().count(i) >= 2:
            str1 += ")"
        else:
            str1 += "("
    return str1


# print(duplicate_encode("Success"))


# reasonably sure its O(n)
def duplicate_encode2(word):
    word = word.lower()
    char_dict = {}
    for i in word:
        # average of O(1) complexity of in set/dict
        char_dict[i] = ")" if i in char_dict else "("
    print(char_dict)
    return "".join(char_dict[i] for i in word)


print(duplicate_encode2("Success"))