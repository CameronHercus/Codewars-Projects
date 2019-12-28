def expanded_form(num):
    return " + ".join(reversed([d + "0" * i for i, d in enumerate(str(num)[::-1]) if d != "0"]))


# print(expanded_form(70304))

