def maxProduct(words):
    return max((len(a) * len(b) for a, b in product(words, words) if set(a).isdisjoint(set(b))), default=0)
# Runtime: 5428 ms, faster than 11.57% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.3 MB, less than 78.84% of Python3 online submissions for Maximum Product of Word Lengths.
