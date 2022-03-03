def minCostToMoveChips(ns):
    res = [0, 0]
    for n in ns:
        res[n&1] += 1
    return res[0] if res[0] < res[1] else res[1]
# runtime beats 99.40 % of python3 submissions
# memory usage beats 77.62 % of python3 submissions.
