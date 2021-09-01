"""
7 Kyu - You're a square!

A square of squares
You like building blocks. You especially like building blocks that are squares.
And what you even like more, is to arrange them 
into a square of square building blocks!

However, sometimes, you can't arrange them into a square.
Instead, you end up with an ordinary rectangle! 
Those blasted things! If you just had a way to know, 
whether you're currently working in vain… Wait! 
That's it! 
You just have to check if your number of building blocks is a perfect square.
"""
import math
def is_square(n):  
    if n > -1 and math.sqrt(n) % 1 == 0:
        return True
    return False

print(is_square(-1))
print(is_square(493193))
