from typing import *
from sys import argv

# O(1) space O(L*k) time
#def rotate(nums: List[int], k: int) -> None:
#    L = len(nums)
#    k = k % L
#    for j in range(k):
#        for i in reversed(range(L - 1)):
#            kprime = (i - 1) % L
#            nums[i] = nums[i] ^ nums[kprime]
#            nums[kprime] = nums[i] ^ nums[kprime]
#            nums[i] = nums[i] ^ nums[kprime]
# Time limit exceeded

# O(L) space O(L) time
#def rotate(nums: List[int], k: int) -> None:
#    L = len(nums)
#    k = k % L
#    if k:
#        acc = []
#        for i in range(L):
#            kprime = (i - k) % L
#            acc.append(nums[kprime])
#        for i in range(L):
#            nums[i] = acc[i]
# Runtime: 318ms, Memoru Usage: 25.6MB

# Slick Python type code
def rotate(nums: List[int], k: int) -> None:
    L = len(nums)
    k = k % L
    acc = nums[(L-k):] + nums
    for i in range(L):
        nums[i] = acc[i]
# Runtime: 342ms, Memory Usage: 25.4MB 🙄

# O(L) time O(1) space with XOR swap... if I can make it work
# for all i, nums[i] must become nums[i-k % L], but can't retrace steps?
#def rotate(nums: List[int], k: int) -> None:
#    L = len(nums)
#    k = k % L
#    if not k:
#        return
#    for i in range(k, L):
#        kprime = (i - k) % L
#        nums[i] = nums[i] ^ nums[kprime]
#        nums[kprime] = nums[i] ^ nums[kprime]
#        nums[i] = nums[i] ^ nums[kprime]
# Couldn't figure this one out, but the solution from the Leetcode forum
# with in-place swap has basically the same performance profile as the
# one above...
# Also one never needs to XOR swap in python, because:
# 'a, b = b, a' swaps a and b 🙄

nums = list(range(1, 5))
k = int(argv[1])
print(nums)
rotate(nums, k)
print(nums)
