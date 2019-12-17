def snail(snail_map):
    """algorithm that takes an array of equal-length sub-arrays,
     and then merges them into a single array in a clockwise spiral,
     starting from the upper-left hand corner"""
    blank = []
    while len(snail_map) > 0:
        blank.extend(snail_map.pop(0))
        for i in range(len(snail_map)):
            blank.append(snail_map[i].pop())
        if len(snail_map) != 0:
            blank.extend(snail_map.pop()[::-1])
        for i in range(len(snail_map) - 1, -1, -1):
            blank.append(snail_map[i].pop(0))
    return blank


"""
array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(snail(array))
"""
