from typing import *

# ez pz Counter version
#Runtime: 32 ms, faster than 89.14% of Python3 online submissions for Find the Difference.
#Memory Usage: 13.9 MB, less than 96.95% of Python3 online submissions for Find the Difference.
from collections import Counter
def findTheDifference(s: str, t: str) -> str:
    return (Counter(t) - Counter(s)).most_common()[0][0]



print(findTheDifference("", "y"))
print(findTheDifference("hello", "hellon"))
