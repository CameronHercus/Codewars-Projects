def max_rot(n):
    blank = []
    blank.append(str(n))
    for i in range(len(str(n))-1):
        blank.append(blank[-1][0:i] + blank[-1][i+1:] + blank[-1][i])
    return max([int(i) for i in blank])

print(max_rot(56789))