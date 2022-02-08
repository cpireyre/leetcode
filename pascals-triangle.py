from typing import *
from math import factorial
# Lol
def generate(numRows: int) -> List[List[int]]:
    return [[1 if k == r or k == 0 else factoral(r)//(factoral(k) * factoral(r - k)) for k in range(0, r + 1)] for r in range(0, numRows)]
#Runtime: 43 ms, faster than 42.67% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.9 MB, less than 85.11% of Python3 online submissions for Pascal's Triangle.

from sys import argv
print(generate(int(argv[1])))
