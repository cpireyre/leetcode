from typing import *
from math import factorial
# Lol
#def generate(numRows: int) -> List[List[int]]:
#    return [[1 if k == r or k == 0 else factorial(r)//(factorial(k) * factorial(r - k)) for k in range(0, r + 1)] for r in range(0, numRows)]
#Runtime: 46 ms, faster than 36.21% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.7 MB, less than 99.71% of Python3 online submissions for Pascal's Triangle.

# Somebody's submission from Leetcode that I cleaned up substantially
def generate(numRows: int) -> List[List[int]]:
    dp = [[1]] + [[1] + [0] * (i - 2) + [1] for i in range(2, numRows + 1)]
    for i in range(2, numRows):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp
#Runtime: 56 ms, faster than 15.41% of Python3 online submissions for Pascal's Triangle.
#Memory Usage: 13.8 MB, less than 94.95% of Python3 online submissions for Pascal's Triangle.

from sys import argv
print(generate(int(argv[1])))
