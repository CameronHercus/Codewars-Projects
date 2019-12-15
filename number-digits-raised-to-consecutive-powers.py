def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    final = []
    for i in range(a, b+1, 1):
        sum_num = 0
        descend_count = len(str(i))
        remainder = i
        while remainder:
            remainder, digit = divmod(remainder, 10)
            sum_num += (digit ** descend_count)
            descend_count -= 1
        if sum_num == i:
            final.append(sum_num)
    return final
#print(sum_dig_pow(1, 89))

