from typing import *
from collections import deque

# Runtime: 73 ms, faster than 55.28% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.9 MB, less than 97.93% of Python3 online submissions for Palindrome Number.
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True

    digits = deque()
    while x:
        digits.append(x % 10)
        x //= 10

    while len(digits) > 1:
        if digits.pop() != digits.popleft():
            return False

    return True

#from sys import argv
#print(isPalindrome(int(argv[1])))
