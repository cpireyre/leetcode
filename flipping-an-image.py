def flipAndInvertImage(image):
    return [[i ^ 1 for i in reversed(row)] for row in image]
# Runtime: 44 ms, faster than 99.03% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.9 MB, less than 75.56% of Python3 online submissions for Flipping an Image.

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
