from typing import *
from math import log2

# Galaxy brain but somehow too slow:
#def findMaximumXor(nums: List[int]) -> int:
#
#    l = len(nums)
#    if l == 2:
#        return nums[0] ^ nums[1]
#    elif l == 1:
#        return 0
#
#    def powerOf2(n: int):
#        p = 0
#        while n:
#            n = n >> 1
#            p += 1
#        return p
#
#    X = [x ^ y for x in nums for y in nums
#            if powerOf2(x) <= powerOf2(y)
#            and x <= y]
#    return(max(X))

# Simple version, also too slow
#def findMaximumXOR(nums: List[int]) -> int:
#    l, localMax, globalMax = len(nums), 0, 0
#    for i in range(0, l - 1):
#        gen = (nums[i] ^ nums[k] for k in range(i + 1, l))
#        localMax = max(gen)
#        globalMax = max(localMax, globalMax)
#    return globalMax

# Greedy with powers of 2. Also too slow.
#def findMaximumXOR(nums: List[int]) -> int:
#    def powerOf2(n: int):
#        p = 0
#        while n:
#            n = n >> 1
#            p += 1
#        return p
#
#    l, localMax, globalMax, i = len(nums), 0, 0, 0
#    nums = sorted(nums, reverse=True)
#    maxP = powerOf2(nums[0])
#    while i < l and powerOf2(nums[i]) == maxP:
#        gen = [nums[i] ^ nums[k] for k in range(i + 1, l)]
#        if gen: localMax = max(gen)
#        globalMax = max(localMax, globalMax)
#        i += 1
#    return globalMax
#

#X = [14,70,53,83,49,91,36,80,92,51,66,70]
#print(findMaximumXOR(X))
#X = [1, 1]
#print(findMaximumXOR(X))
#X = [4]
#print(findMaximumXOR(X))
#X = [3,10,5,25,2,8]
#print(findMaximumXOR(X))
#X = [x + 1000 for x in range(980, 1015)]
#print(findMaximumXOR(X))

   
# Well I thought about this all day and I couldn't figure it out, so
# I'm copy pasting this one from Leetcode:
def findMaximumXOR(self, nums: List[int]) -> int:
    """
    
    mashup of hamming distance like problems and 2sum.
    
    take advantage of the 32 bit representation of the numbers in question
    
    generate bits starting 100000000, 110000000.... 111111111
        
    we want 1 on the lsb (on the left side)
    so we iterate a full 32 bits and set up
    
    find pair -> find max possible xor till ith index
    
    commutative group properties (with action = xor)
    a^b = c; b^c = a; a^c = b
    where:
    a = prefix of arr[j] till ith
    b = maxPossible xor till ith-1 + set ith bit
    
    This is important since we're asking is there 2 numbers with the prefix.
    
    Time: O(32N) -> O(N)
    
    """

    maximum = 0
    mask = 0
    
    for i in range(30, -1, -1):
        one = 1 << i
        mask = mask | one   
        
        # generate prefixes with bitwise mask for ith bit
        prefixes = set()
        for num in nums:
            # bitwise and will clear except relevent bits in mask
            prefixes.add(mask & num)
            
        # corresponds to ith bit of maximum
        test = maximum | one
        
        # now traverse the prefixes, ask, is there two numbers with a opposite 
        # prefix.
        for prefix in prefixes:
            # like two sum
            # confirm that we have two numbers with the opposite bits
            if prefix ^ test in prefixes:
                maximum = test
                break
                
    return maximum
