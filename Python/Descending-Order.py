# 1st attempt
def descending_order(num):
    return int("".join(x for x in sorted(list(str(num)), reverse=True)))


# 2nd attempt
def descending_order(num):
    return int("".join(x for x in sorted(str(num), reverse=True)))
