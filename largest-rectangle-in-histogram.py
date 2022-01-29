# If a solution includes H[i], then the upper bound
# for that solution is n * H[i]
# The lower bound for any solution is n * H[min]
# First idea: Start somewhere, walk the array in both directions,
# stop when you get to an index such that including it would lower
# the area. Complexity: somewhere between O(n^2) and O(n)???
# Area between H[n] and H[m] = (m - n + 1) * min(H[k]) for n <= k <= m
# Only worth adding the next bar if: it's bigger OR ???
# if n * min(H[k -> k + p]) <= (n + 1) min(H[k -> k + p + 1])
# You can brute force in n(n+1)/2 operations, find min then multiply
# If there was a way to cache the min lookup, it might be fast enough
# Dynamic programming time?
# Fastest way to label min for every contiguous n-uple basically
# If global min = k => for all n>0 and all p>0, min (k - n -> k + p) = k
# min(L1 + L2) = min(min(L1), min(L2))

# Brute force, just for laughs:
#def largestRectangleArea(heights: List[int]) -> int:
#    rectangles = [heights[n:n+p+1]
#            for n in range(0, len(heights))
#            for p in range(len(heights) - n)]
#    areas = map(lambda l: len(l) * min(l), rectangles)
#    return max(areas)
# "Memory limit exceeded"


#length = len(heights)
#splits = [(heights[0:n], heights[n+1:length]) for n in range(1,length-1)]
#print(splits)

from typing import *
#from functools import cache
# New plan: for a given slice, compute min and area and cache the result
#def largestRectangleArea(heights: List[int]) -> int:
#
#    @cache
#    def recursiveSliceMin(start: int, end: int) -> int:
#        if start == end:
#            return heights[start]
#        else:
#            return min(heights[start], recursiveSliceMin(start + 1, end))
#
#    L = len(heights)
#    lowerBound = max(heights)
#    for sliceLength in range(1, L):
#        sliceGen = ((1 + sliceLength) * recursiveSliceMin(k, k + sliceLength) for k in range(L - sliceLength))
#        localMax = max(sliceGen)
#        if localMax > lowerBound:
#            lowerBound = localMax
#
#    return lowerBound
# Memory limit exceeded on an array full of 1s. recursiveSliceMin blew up
# It shouldn't have though?

#heights = [2,1,5,6,2,3]
#print(largestRectangleArea(heights))
#heights = [2,4]
#print(largestRectangleArea(heights))
#heights = [100000]
#print(largestRectangleArea(heights))

# I couldn't get this one. Copy pasting from Leetcode.
# One has to use what is called a "monotonic stack"

def largestRectangleArea(self, bars: List[int]) -> int:
	st, res = [], 0
	for bar in bars + [-1]: # add -1 to have an additional iteration
		step = 0
		while st and st[-1][1] >= bar:
			w, h = st.pop()
			step += w
			res = max(res, step * h)

		st.append((step + 1, bar))

	return res
