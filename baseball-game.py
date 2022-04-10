from functools import reduce
def calPoints(ops):
    def step(acc, op):
        if op == "+":
            return acc + [int(acc[-1]) + int(acc[-2])]
        elif op == "D":
            return acc + [2 * int(acc[-1])]
        elif op == "C":
            return acc[0:len(acc) - 1]
        else:
            return acc + [int(op)]
    return sum(reduce(step, ops, []))
# Runtime: 89 ms, faster than 12.66% of Python3 online submissions for Baseball Game.
# Memory Usage: 14 MB, less than 74.69% of Python3 online submissions for Baseball Game.

ops = ["5","2","C","D","+"]
print(calPoints(ops)) # 30
ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops)) # 27
ops = ["1"]
print(calPoints(ops)) # 1
