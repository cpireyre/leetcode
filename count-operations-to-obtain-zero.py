# dumb recur ver
# def countOperations(num1, num2):
#     print(num1, num2)
#     if not num1 or not num2:
#         return 0
#     else:
#         if num1 < num2:
#             num1, num2 = num2, num1
#         return 1 + countOperations(num1 - num2, num2)
# Runtime: 405 ms, faster than 7.91% of Python3 online submissions for Count Operations to Obtain Zero.
# Memory Usage: 117.3 MB, less than 6.17% of Python3 online submissions for Count Operations to Obtain Zero.

# Copying and pasting my own code from Foobar ver:
def countOperations(x, y):
    def retrace(x, y, generations=0):
        if not x or not y:
            return (x, y, generations)
        if x < y:
            x, y = y, x
        return retrace(x % y, y, generations + x // y)
    return retrace(x, y)[2]
# Runtime: 28 ms, faster than 99.39% of Python3 online submissions for Count Operations to Obtain Zero.
# Memory Usage: 13.9 MB, less than 66.43% of Python3 online submissions for Count Operations to Obtain Zero.
