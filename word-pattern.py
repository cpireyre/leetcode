def checkPattern(a, b, d) -> bool:
    if not a and not b:
        return True
    currA = a.pop()
    currB = b.pop()
    if currA in d:
        return d[currA] == currB and checkPattern(a, b, d)
    else:
        return currB not in d.values() and checkPattern(a, b, d | (currA, currB))

def wordPattern(pattern: str, s: str) -> bool:
    return checkPattern(list(pattern), s.split(), dict())

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
