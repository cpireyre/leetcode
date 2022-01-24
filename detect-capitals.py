# caps = 65 to 90 inclusive
# smols = 97 to 122 inclusive
from sys import argv
s = argv[1]

# Slow version with sets:
# def detectCapitalUse(word):
#     caps = {chr(x) for x in range(65, 91)}
#     mins = {chr(x) for x in range(97, 123)}
#     first = word[0] in caps
#     if first:
#         return set(word) <= caps or set(word[1:]) <= mins
#     else:
#         return set(word) <= mins

# Fast (hopefully) version with booleans:
# XOR: p^q
# XNOR = not (p^q)
# P = first letter is cap
# Q = all the remaining letters are the same

def detectCapitalUse(word):
    b = bytes(word, 'ascii')
    prev = 65 <= b[0] <= 90
    for i in range(1, len(b)):
        curr = 65 <= b[i] <= 90
        if prev ^ curr and (not prev or i > 1):
            return False
        prev = curr
    return True

# This turned out to be in the 98th percentile for memory usage,
# but fairly low for runtime.
# Everyone else was calling string functions directly, so the overhead
# here must be coming from the "bytes" call which implies re-enconding the string.
# I tried using ord() but it had even worse overhead which I don't understand how
# that's possible.
# It seems the Python interpreter basically never does inlining.


#print(detectCapitalUse(argv[1]))
