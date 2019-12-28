def compareTriplets(a, b):
    counter_a = 0
    counter_b = 0
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            counter_a += 1
        elif b[i] > a[i]:
            counter_b += 1
    return [counter_a, counter_b]

# print(compareTriplets([1,1,1], [1,2,3,11,1,1,1,1,1,11,1,1,]))