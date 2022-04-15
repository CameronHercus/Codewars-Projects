def longest_consec(strarr, k):
    """6kyu"""
    if len(strarr) > 0 and k < len(strarr) and k > 0:
        blank = []
        for i in range(len(strarr[0:-k])):
            blank.append("".join(strarr[i:i+k]))
        blank.append("".join(strarr[-k:]))
        return max(blank, key=len)
    return ""

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))