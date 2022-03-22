from itertools import combinations
def maxProduct(words):
    def bin(s):
        res = 0
        for c in s:
            res |= 1 << (ord(c) - 97)
        return res
    return max((la * lb for (la, ba), (lb, bb) in combinations(((len(a), bin(a)) for a in words), 2) if not ba & bb), default=0)
# Runtime: 370 ms, faster than 89.19% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.4 MB, less than 50.08% of Python3 online submissions for Maximum Product of Word Lengths.

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(maxProduct(words))
