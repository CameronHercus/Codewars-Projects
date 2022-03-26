"""
6 kyu - How many pages in a book?
"""


def amount_of_pages(summary):
    """6 kyu - How many pages in a book?"""
    counter = 0
    for i in range(1, summary+1, 1):
        counter += len(str(i))
        if counter >= summary:
            return i
    return None
print(amount_of_pages(25 ))