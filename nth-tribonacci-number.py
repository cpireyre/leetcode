from functools import @cache
@cache
def tribonacci(n):
    if n == 0: return 0
    elif n <= 2: return 1
    else: return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
# Runtime: 64 ms, faster than 5.17% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.6 MB, less than 99.98% of Python3 online submissions for N-th Tribonacci Number.
