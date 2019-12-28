# 1st attempt
def rgb(r, g, b):
    r, g, b = map(lambda x: 0 if x < 0 else 255 if x > 255 else x, [r, g, b])
    return "{:02X}{:02X}{:02X}".format(r, g, b)


# second attempt
def rgb(r, g, b):
    rounded = lambda x: min(255, max(x, 0))
    return "{:02X}{:02X}{:02X}".format(rounded(r), rounded(g), rounded(b))
