def in_array(array1, array2):
    r = []
    for x in array1:
        for y in array2:
            if x not in r:
                if x in y:
                    r.append(x)
    return sorted(r)


# more time efficient preferred solution
def in_array2(array1, array2):
    r = {}
    for sub in array1:
        if sub not in r:
            for full_str in array2:
                if sub in full_str:
                    r[sub] = ""
    return sorted(r)


# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# print(in_array2(a1, a2))
# print(in_array(a1, a2))
