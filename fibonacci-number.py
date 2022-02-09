class Solution:
    @cache
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n - 1) + self.fib(n - 2)
#Runtime: 54 ms, faster than 38.21% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 13.9 MB, less than 92.30% of Python3 online submissions for Fibonacci Number.
