def removeCoveredIntervals(intervals):
    def intKey(i):
        return (i[0], -i[1])

    def covers(a, b):
        return a[0] <= b[0] < b[1] <= a[1]

    def removeRecur(ts):
        if not ts:
            return 0
        return 1 + removeRecur([i for i in ts[1:] if not covers(ts[0], i)])

    return removeRecur(sorted((tuple(i) for i in intervals), key=intKey))
# Runtime: 96 ms, faster than 85.97% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.8 MB, less than 59.22% of Python3 online submissions for Remove Covered Intervals.


intervals = [[1, 4], [3, 6], [2, 8]]
print(removeCoveredIntervals(intervals))
intervals = [
    [34335, 39239],
    [15875, 91969],
    [29673, 66453],
    [53548, 69161],
    [40618, 93111],
]
print(removeCoveredIntervals(intervals))
intervals = [[1, 2], [1, 4], [3, 4]]
print(removeCoveredIntervals(intervals))
