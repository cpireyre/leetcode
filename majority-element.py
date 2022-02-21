from collections import Counter
def majorityElement(ns):
    return Counter(ns).most_common()[0][0]
# Runtime: 246 ms, faster than 42.16% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.
