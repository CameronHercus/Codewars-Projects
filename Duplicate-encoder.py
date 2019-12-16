def duplicate_encode(word):
    str1 = ""
    for i in word.lower():
        # .count will always be O(n) so could be improved to terminate at freq at 2
        if word.lower().count(i) >= 2:
            str1 += ")"
        else:
            str1 += "("
    return str1
# make lambda func that calls and then formats {}* len of word
print(duplicate_encode("Success"))