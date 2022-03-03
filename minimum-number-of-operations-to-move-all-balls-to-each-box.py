def minOperations(boxes):
    ones = [i for i, c in enumerate(boxes) if c == '1']
    return [sum(abs(i - j) for j in ones) for i in range(len(boxes))]
# Runtime: 2124 ms, faster than 54.98% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
# Memory Usage: 14.3 MB, less than 52.28% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.

boxes = "001011"
print(minOperations(boxes))
