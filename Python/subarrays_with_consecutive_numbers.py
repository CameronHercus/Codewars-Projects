def range_extraction(args):
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


print(range_extraction(
    [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
