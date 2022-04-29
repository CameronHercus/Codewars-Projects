def move_zeros(array):
    return [i for i in array if i != 0] + [j for j in array if j == 0]

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))