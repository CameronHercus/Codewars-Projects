import re


def increment_string(strng):
    digits = re.findall(r'\d+', strng)
    if digits:
        og_number = digits[-1]
        strng = strng.rsplt(og_number, 1)[0]
        new_number = str(int(og_number) + 1)
        return strng + "0" * (len(og_number) - len(new_number)) + new_number
    else:
        return strng + "1"


# need it to check just the last digit and if its 9 it needs to change otherwise just do str(int(index) + 1)
print((increment_string("foobar0099")))
print((increment_string("foobar01")))
print((increment_string("")))
print((increment_string("foo")))
