"""
6 kyu - Count Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that
occur more than once in the input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.
"""


def duplicate_count(text):
    comparison_set = set()
    counter_set = set()
    for i in text:
        if i not in comparison_set:
            if i.isalpha():
                comparison_set.add(i.lower())
                comparison_set.add(i.upper())
            else:
                comparison_set.add(i)
        else:
            if i.isalpha():
                counter_set.add(i.upper())
            else:
                counter_set.add(i)
    return len(counter_set)

print(duplicate_count("abcdeaB"))
