








def unique_in_order(iterable):
    prev = None
    blank = []
    for i in iterable:
        if i != prev:
            blank.append(i)
            prev = i
    return blank

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))
