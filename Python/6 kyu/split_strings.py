"""
6 kyu - Split Strings
"""


def solution(s):
    """6 kyu - Split Strings"""
    blank = []
    final = []
    for i, j in enumerate(s):
        if i % 2 == 0:
            blank.append(j)
        else:
            blank.append(j)
            final.append("".join(blank))
            blank = []
    if len(blank) != 0:
        blank.append("_")
        final.append("".join(blank))
    return final

    
print(solution("asdfads"))