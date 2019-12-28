def namelist(names):
    if len(names) > 1:
        str1 = ", ".join([j + " & " + names[-1]["name"] if i+2 == len(names) else j for i, j in enumerate(d["name"] for d in names[:-1])])
    elif len(names) == 1:
        str1 = names[0]["name"]
    else:
        str1 = ""
    return str1


print(namelist([{'name': 'Bart'}]))