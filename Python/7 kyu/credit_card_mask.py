# return masked string
def maskify(cc):
    """7 kyu - Credit Card Mask"""
    blank = list(cc)
    for i in range(len(blank[0:-4])):
        blank[i] = "#"
    return "".join(blank)
print(maskify("4556364607935616"))