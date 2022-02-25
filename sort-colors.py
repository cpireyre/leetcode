# sorting ? never heard of her ver
from collections import Counter
def sortColors(ns):
    c = Counter(ns)
    red, white, blue = c[0], c[1], c[2]
    i = 0
    while red or white or blue:
        if red:
            ns[i] = 0
            red -= 1
        elif white:
            ns[i] = 1
            white -= 1
        else:
            ns[i] = 2
            blue -= 1
        i += 1
# Runtime: 32 ms, faster than 92.11% of Python3 online submissions for Sort Colors.
# Memory Usage: 13.9 MB, less than 61.30% of Python3 online submissions for Sort Colors.
