import re
def count_smileys(arr):
    """6 kyu - Count the smiley faces!"""
    return len(re.findall('[:;][-~]?[)D]', str(arr)))


print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
