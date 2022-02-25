# One liner to scare the normies
from itertools import zip_longest


def compareVersions(v1, v2):
    return next( ( (a - b) // abs(a - b) for a, b in zip_longest( map(int, v1.split(".")), map(int, v2.split(".")), fillvalue=0) if a != b), 0,)
# Runtime: 32 ms, faster than 83.77% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 68.52% of Python3 online submissions for Compare Version Numbers.


version1 = "1.01"
version2 = "1.001"
print(compareVersions(version1, version2))
version1 = "1.0"
version2 = "1.0.0"
print(compareVersions(version1, version2))
version1 = "0.1"
version2 = "1.1"
print(compareVersions(version1, version2))
