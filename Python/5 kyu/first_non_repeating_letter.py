def first_non_repeating_letter(string):
    """"""
    lower_string = "".join([i.lower() for i in string])
    for i in string:
        if lower_string.count(i.lower()) == 1:
            return i
    return ''

print(first_non_repeating_letter('sTreSS'))