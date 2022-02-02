# Something like a sliding window that's also a Counter that's also a Deque...
# If S[2,12] is an anagram, then S[3,13] is an anagram iff S[2] == S[13]
# Each character you read constrains the ones to follow until you get an anagram
# or you get an illegal sequence in which case you know no one can be an anagram
# in between there and here

from typing import *
from collections import Counter

# Short version with sliding window generator, unoptimized
#def findAnagrams(s: str, p: str) -> List[int]:
#    lp, ls, p = len(p), len(s), Counter(p)
#    res = [x[1]
#            for x in ((s[i:i+lp], i) for i in range(0, ls - lp + 1))
#            if Counter(x[0]) == p]
#    return res
# Time limit exceeded, yeah I didn't think so

#Runtime: 245 ms, faster than 25.28% of Python3 online submissions for Find All Anagrams in a String.
#Memory Usage: 15.3 MB, less than 10.05% of Python3 online submissions for Find All Anagrams in a String.
def findAnagrams(s: str, p: str) -> List[int]:
    lp, ls, p, offset = len(p), len(s), Counter(p), 0
    res = []
    p.subtract(Counter(s[:lp])) # svo Pythonic 🙄

    # If p.values() returns a list in linear time then F lol
    if not any(p.values()): res.append(0)
    while offset + lp < ls:
        p[s[offset]] += 1
        p[s[offset + lp]] -= 1
        offset += 1
        if not any(p.values()):
            res.append(offset)

    return res

# methods like .values() return a "view object" which is:
# - not a list
# - not an iterator
# - not a generator
# is .values() constant time??? Linear??? Who knows????

from sys import argv
print(findAnagrams(argv[1], argv[2]))
