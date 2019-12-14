# 1st attempt
def create_phone_number(n):
    string = "".join(str(x) for x in n)

    return "(" + string[0:3] + ") " + string[3:6] + "-" + string[6:]
