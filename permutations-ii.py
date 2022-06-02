from itertools import permutations
def permuteUnique(ns):
    return list({_ for _ in permutations(ns)})
# Runtime: 77 ms, faster than 66.00% of Python3 online submissions for Permutations II.
# Memory Usage: 14 MB, less than 95.20% of Python3 online submissions for Permutations II.
