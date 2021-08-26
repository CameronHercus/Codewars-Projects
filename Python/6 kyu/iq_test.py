"""
6 kyu - IQ Test
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
 differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check
 his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a
 position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start
from 1 (not 0)
"""


def iq_test(numbers):
    # Assumes there will always be >=3 length of numbers
    blank = [int(x) for x in numbers.split(" ")]
    first_3 = blank[0] % 2 + blank[1] % 2 + blank[2] % 2
    if first_3 < 2:
        remainder = 1
    else:
        remainder = 0
    for i in range(len(blank)):
        if blank[i] % 2 == remainder:
            return i + 1
    return None


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 2"))
