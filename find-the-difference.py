from typing import *

# ez pz Counter version
#Runtime: 32 ms, faster than 89.14% of Python3 online submissions for Find the Difference.
#Memory Usage: 13.9 MB, less than 96.95% of Python3 online submissions for Find the Difference.
#from collections import Counter
#def findTheDifference(s: str, t: str) -> str:
#    return (Counter(t) - Counter(s)).most_common()[0][0]

# bit array tedious version
# change to byte array or iterate on string directly?
# if iterating on string, must call ord() each time: big overhead?
# you would think same overhead but not in practice
#Runtime: 40 ms, faster than 60.50% of Python3 online submissions for Find the Difference.
#Memory Usage: 13.9 MB, less than 88.02% of Python3 online submissions for Find the Difference.
# I think faster in the average case but not always. Worse memory footprint.
#from math import log2
#def findTheDifference(s: str, t: str) -> str:
#    i = len(s)
#    s = bytearray(s, encoding="ascii")
#    t = bytearray(t, encoding="ascii")
#    ans = 1 << t[i] - 97
#    i -= 1
#    while i >= 0:
#        ans ^= (1 << (t[i] - 97)) ^ (1 << (s[i] - 97))
#        i -= 1
#    return chr(int(log2(ans)) + 97)

# functional ivory tower code ver
#Runtime: 32 ms, faster than 89.14% of Python3 online submissions for Find the Difference.
#Memory Usage: 13.9 MB, less than 88.02% of Python3 online submissions for Find the Difference.
# Huge variance though, sometimes slower than everything else
from functools import reduce
def findTheDifference(s: str, t: str) -> str:
    return chr(reduce(lambda a,b: a^b, bytearray(s + t, encoding="ascii")))

print(findTheDifference("helloworld", "helzloworld"))
print(findTheDifference("hello", "hellon"))
print(findTheDifference("", "y"))
print(findTheDifference("", "c"))
