def transpose(matrix):
    # ret = []
    # for i in range(len(matrix[0])):
    #     ret.append([row[i] for row in matrix])
    # return ret
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Runtime: 160 ms, faster than 6.75% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.8 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))
matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))
