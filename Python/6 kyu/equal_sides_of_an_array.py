def find_even_index(arr):
    """6 kyu - Equal Sides Of An Array"""
    sum1 = 0
    sum2 = 0

    for i in range(0, len(arr), 1):
        sum1 = sum(arr[i+1:])
        sum2= sum(arr[0:i])
        if sum1 == sum2:
            print(i)
    return ""


print(find_even_index([1,2,3,4,3,2,1]))