# next time just use .bit_length() and .bit_count() 🙄
def numberOfSteps(n):
    return n if n <= 3 else sum((n >= 1<<i) * (1 + (not not (n & 1<<i))) for i in range(25)) - 1
# Runtime: 44 ms, faster than 50.22% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 98.14% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

from sys import argv
print(numberOfSteps(int(argv[1])))
