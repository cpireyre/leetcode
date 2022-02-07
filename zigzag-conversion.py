from typing import *
from itertools import cycle
#Runtime: 59 ms, faster than 82.66% of Python3 online submissions for Zigzag Conversion.
#Memory Usage: 14.1 MB, less than 85.03% of Python3 online submissions for Zigzag Conversion.
def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    ret = [""] * numRows
    index = cycle(list(range(numRows - 1)) + list(reversed(range(1, numRows))))
    for i, c in zip(index, s):
        ret[i] += c
        #print("That's right, adding %c to %i" % (c, i))
    #for p in ret:
        #print(p)
    return ''.join(ret)

from sys import argv
print(convert(argv[1],3))
