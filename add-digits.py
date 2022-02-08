from typing import *
#Math ver
#def addDigits(num: int) -> int:
#    if num < 10: return num
#    else:
#        acc = 0
#        while num:
#            acc += num % 10
#            num //= 10
#        return addDigits(acc)
#Runtime: 39 ms, faster than 53.25% of Python3 online submissions for Add Digits.
#Memory Usage: 13.8 MB, less than 91.66% of Python3 online submissions for Add Digits.

# Sum map ord one-liner ver
#def addDigits(num: int) -> int:
    #return num if num < 10 else self.addDigits(sum(map(lambda a: ord(a) - ord('0'), str(num))))
#Runtime: 66 ms, faster than 8.01% of Python3 online submissions for Add Digits.
#Memory Usage: 13.8 MB, less than 99.39% of Python3 online submissions for Add Digits.

# Brainlet loop ver
#def addDigits(num: int) -> int:
#    while num > 9:
#        acc = 0
#        while num:
#            acc += num % 10
#            num //= 10
#        num = acc
#    return num
#Runtime: 27 ms, faster than 94.47% of Python3 online submissions for Add Digits.
#Memory Usage: 13.9 MB, less than 91.66% of Python3 online submissions for Add Digits.
# Big variance so this performance is contrived but whatever

# Takewhile ver
from itertools import takewhile, count
def addDigits(num: int) -> int:
    return num if num <= 9 else sum(map(lambda x: x % 10, takewhile(lambda x: x, (num//q for q in (10**p for p in count(0))))))
#Runtime: 55 ms, faster than 24.58% of Python3 online submissions for Add Digits.
#Memory Usage: 13.8 MB, less than 99.39% of Python3 online submissions for Add Digits.

from sys import argv
print(addDigits(int(argv[1])))
