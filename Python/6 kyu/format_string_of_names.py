"""
6 kyu - Format a string of names like 'Bart, Lisa & Maggie'.

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
"""


def namelist(names):
    if len(names) > 1:
        str1 = ", ".join([j + " & " + names[-1]["name"]
                          if i + 2 == len(names) else j for i, j in enumerate(d["name"] for d in names)
                          if i + 1 != len(names)])
    elif len(names) == 1:
        str1 = names[0]["name"]
    else:
        str1 = ""
    return str1
