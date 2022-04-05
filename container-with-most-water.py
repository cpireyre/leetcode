def maxArea(height):
    l, r = 0, len(height) - 1
    A = 0
    while l < r:
        A = max(A, min(height[l], height[r]) * (r - l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return A
# Runtime: 937 ms, faster than 53.40% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 58.32% of Python3 online submissions for Container With Most Water.

height = [1,8,6,2,5,4,8,3,7] # 49
print(maxArea(height))
height = [1,1] # 1
print(maxArea(height))
