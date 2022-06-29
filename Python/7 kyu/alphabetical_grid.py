"""
7 kyu - Alphabetical Grid
"""
import string


def grid(N):
    """7 kyu - Alphabetical Grid"""
    if N >= 0:
        alpha_list = string.ascii_lowercase
        return "\n".join(" ".join([alpha_list[j%26] for j in range(i, N+i)]) for i in range(N))
    return None

#Attempt 1
def grid(N):
    """7 kyu - Alphabetical Grid"""
    if N < 0:
        return None
    result = string.ascii_lowercase
    blank = []
    final = []
    counter = 0
    for i in range(N):
        counter = i
        for j in range(N):
            if counter > 25:
                counter = counter % 26
            blank.append(result[counter])
            counter += 1
        final.append(" ".join(blank))
        blank = []
    return "\n".join(final)


print(grid(30))