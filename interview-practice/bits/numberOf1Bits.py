def numberOf1Bits(n):
    res = 0
    while n != 0:
        n &= n-1
        res += 1
    return res