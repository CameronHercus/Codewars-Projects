# 1st attempt
def solution(number):
    sum = 0
    for i in range(1, number, 1):
        print(i)
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i

    return sum
