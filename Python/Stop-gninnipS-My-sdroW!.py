def spin_words(sentence):
    reverse_string = lambda x: x[::-1]
    return " ".join([i if len(i) < 5 else reverse_string(i) for i in sentence.split()])
# print(spin_words( "Hey fellow warriors" ))
