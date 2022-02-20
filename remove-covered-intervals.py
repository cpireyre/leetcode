# Atrocious one liner to scare the normies
def removeCoveredIntervals(intervals):
    def removeRecur(ts):
        return 1 + removeRecur([i for i in ts[1:] if not ts[0][0] <= i[0] < i[1] <= ts[0][1]]) if ts else 0
    return removeRecur(sorted(intervals, key=lambda i: (i[0], -i[1])))
# Runtime: 110 ms, faster than 67.27% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.4 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
