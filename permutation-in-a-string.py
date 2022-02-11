from typing import *
from collections import Counter

# About as stateless as I can make it I think
# Need to check _out != _in because {a: -1, a: 1} collapses to {a: 1} lol 🙄
def checkInclusion(s1: str, s2: str) -> bool:
    ls1, ls2, c1 = len(s1), len(s2), Counter(s1)
    window = Counter(s2[0:ls1])
    for _out, _in in zip(s2[0:ls2 - ls1], s2[ls1:]):
        if window == c1: return True
        if _out != _in: window.update({_out:-1, _in:1})
    return window == c1 # Don't forget the last one
#Runtime: 144 ms, faster than 43.62% of Python3 online submissions for Permutation in String.
#Memory Usage: 14 MB, less than 93.32% of Python3 online submissions for Permutation in String.

# Could it be faster to update diff and check if 0?
# On assumption (not Counter) runs in constant time and (Counter1 == Counter2) is linear
# Except Counter({1: 0}) == True lol 🙄🤡  meme lang
# Therefore one still has to check all the values... might be marginally faster but
# not worth the effort and hit to clarity.

# One-liner slow ver:
def checkInclusion(s1: str, s2: str) -> bool:
    return any(filter(lambda x: x == Counter(s1), map(Counter, (s2[o:o+len(s1)] for o in range(0, len(s2))))))
#Runtime: 9420 ms, faster than 5.01% of Python3 online submissions for Permutation in String.
#Memory Usage: 13.8 MB, less than 99.16% of Python3 online submissions for Permutation in String.

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2)) # True
s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2)) # False
s1 = "a"
s2 = "ab"
print(checkInclusion(s1, s2)) # True
s1 = "adc"
s2 = "adca"
print(checkInclusion(s1, s2)) # True
s1 = "abc"
s2 = "cccccbabbbaaaa"
print(checkInclusion(s1, s2)) # True
