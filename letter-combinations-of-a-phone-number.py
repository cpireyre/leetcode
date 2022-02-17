from typing import *
from itertools import product
def letterCombinations(digits: str) -> str:
    letters = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("xwyz")
            }
    # *[xs] is like Clojure (apply xs) where it destructures the input
    # iterable into kwargs! Useful.
    return ["".join(p) for p in product(*[letters[c] for c in digits]) if p]
# Runtime: 38 ms, faster than 56.77% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.9 MB, less than 78.03% of Python3 online submissions for Letter Combinations of a Phone Number.

digits = "23"
print(letterCombinations(digits))
digits = ""
print(letterCombinations(digits))
digits = "2"
print(letterCombinations(digits))
