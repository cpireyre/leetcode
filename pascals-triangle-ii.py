from math import factorial
from functools import cache
from typing import *
def getRow(r: int) -> List[int]:
    @cache
    def f(n): return factorial(n)
    return [1 if k == r or k == 0 else f(r)//(f(k) * f(r - k)) for k in range(0, r + 1)]
#Runtime: 32 ms, faster than 79.34% of Python3 online submissions for Pascal's Triangle II.
#Memory Usage: 13.9 MB, less than 85.49% of Python3 online submissions for Pascal's Triangle II.
