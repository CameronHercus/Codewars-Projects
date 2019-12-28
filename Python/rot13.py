def rot13(message):
    #chr((ord(message[0].lower()) - 97 + 13) % 26 + 97)
    blank = []
    for i in message:
        if i != " ":
            if i.islower():
                blank.append(chr((ord(i) - 97 + 13) % 26 + 97))
            else:
                blank.append((chr((ord(i) - 65 + 13) % 26 + 97)).upper())
        else:
            blank.append(" ")
    return "".join(blank)
print(rot13("Test"))
print(rot13("test"))