"""
4 kyu - Range Extraction

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers or a range of integers denoted by the starting integer separated from the end integer in the
range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered
a range unless it spans at least 3 numbers. For example "12,13,15-17" Complete the solution so that it takes a list
of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
// returns "-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""


def solution(args):
    unprocessed = [args[0]]  # the list for candidates for range extraction
    final = []  # The list for processed
    for i in range(1, len(args)):
        if args[i] != unprocessed[-1] + 1:
            process(args[i], final, unprocessed)
        unprocessed.append(args[i])
    process(args[i], final, unprocessed)
    return ",".join(final)


def process(key, final, unprocessed):
    if len(unprocessed) >= 3 and key != unprocessed[-1] + 1:
        final.append(str(unprocessed[0]) + "-" + str(unprocessed[-1]))
        unprocessed.clear()
    else:
        for j in unprocessed:
            final.append(str(j))
        unprocessed.clear()
