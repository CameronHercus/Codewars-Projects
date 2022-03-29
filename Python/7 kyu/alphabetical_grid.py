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

print(grid(30))