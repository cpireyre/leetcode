# caps = 65 to 90 inclusive
# smols = 97 to 122 inclusive
from sys import argv
s = argv[1]

def detectCapitalUse(word):
    caps = {chr(x) for x in range(65, 91)}
    mins = {chr(x) for x in range(97, 123)}
    first = word[0] in caps
    if first:
        return set(word) <= caps or set(word[1:]) <= mins
    else:
        return set(word) <= mins

print(detectCapitalUse(argv[1]))
