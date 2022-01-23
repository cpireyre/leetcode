from math import log10, ceil
from itertools import *
from functools import reduce
from sys import argv

# def sequentialDigitsOfLength(length):
# 
#     acc = 0
#     inc = 0
#     for i in range(1, length + 1):
#         acc *= 10 
#         acc += i
#         inc *= 10
#         inc += 1
# 
#     digits = range(acc, 10**length, inc)
#     return list(digits)[0:(10-length)]
# 
# def sequentialDigitsUpTo(n):
#     length = ceil(log10(n))
#     nums = []
#     for d in range(2, length + 1):
#         nums += sequentialDigitsOfLength(d)
#     return [k for k in nums if k <= n]
# 
# def sequentialDigitsBetween(low, high):
#     nums = sequentialDigitsUpTo(high)
#     return [k for k in nums if k >= low]

#n = int(argv[1])
#print(sequentialDigitsUpTo(n))

# The above works fine but it's ugly. I think it'd be cooler to
# pop everything from a single generator.

def sequentialDigits(low, high):
    initials = islice(accumulate(count(1), lambda a, b: 10*a + b), 1, ceil(log10(high)))
    generators = []

    for i in initials:
        mag = ceil(log10(i))
        start = i
        step = reduce( lambda a, b: 10*a + b, repeat(1, mag))
        seq = islice(count(i, step), 10 - mag)
        generators.append(seq)

    digits = chain.from_iterable(generators)
    digits = dropwhile(lambda x: x < low, digits)
    digits = takewhile(lambda x: x <= high, digits)
    return list(digits)

low = int(argv[1])
high = int(argv[2])
print(sequentialDigits(low, high))

# Performance-wise the above is indistinguishable from the v1 so, F
# Here's a much better take from a Leetcode user:

#   def sequentialDigits(self, low: int, high: int) -> List[int]:
#        queue = collections.deque(list(range(1, 10)))
#        
#        res = []
#        while queue:
#            u = queue.popleft()
#            if low <= u <= high:
#                res.append(u)
#            last_num = u % 10
#            if last_num != 9:
#                queue.append(u * 10 + last_num + 1)
#        return res
