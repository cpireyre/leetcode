# if even x, divide or succ?
# if odd x, succ
def brokenCalc(goal, x):
    return goal - x if x<=goal else 1 + brokenCalc(goal,x+1 if x & 1 else x >> 1)
# Runtime: 54 ms, faster than 24.66% of Python3 online submissions for Broken Calculator.
# Memory Usage: 13.9 MB, less than 73.06% of Python3 online submissions for Broken Calculator.

goal, x = 2, 3 # 2
print(brokenCalc(goal, x))
goal, x = 5, 8 # 2
print(brokenCalc(goal, x))
goal, x = 3, 10 # 3
print(brokenCalc(goal, x))
goal, x = 1000000000, 1
