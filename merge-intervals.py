def merge(intervals):
    intervals.sort(reverse=True)
    res = [intervals.pop()]
    while intervals:
        (a, b), (c, d) = res[-1], intervals.pop()
        if (b >= c) or (a >= d):
            res[-1] = [a if a < c else c, b if b > d else d]
        else:
            res.append([c, d])
    return res
# Runtime: 252 ms, faster than 25.08% of Python3 online submissions for Merge Intervals.
# Memory Usage: 18.1 MB, less than 86.44% of Python3 online submissions for Merge Intervals.



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))
