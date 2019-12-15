def countBits(n):
    return bin(n)[2:].count("1")

print(countBits(10))