"""
6 kyu - Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often
 referred to as Pascal case).
"""


def to_camel_case(text):
    blank = text.replace("_", "-").split("-")
    blank_2 = [blank[0]]
    for i in range(1, len(blank), 1):
        blank_2.append(blank[i][0].upper() + blank[i][1:])
    return "".join(blank_2)


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
