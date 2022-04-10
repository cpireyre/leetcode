from functools import reduce
def calPoints(ops):
    funcs = {
        "+": lambda acc: acc.append(acc[-1] + acc[-2]),
        "D": lambda acc: acc.append(2 * acc[-1]),
        "C": lambda acc: acc.pop()
        }
    acc = []
    for op in ops:
        if op[0] == "-" or op[0].isdigit():
            acc.append(int(op))
        else:
            (funcs[op])(acc)
    return sum(acc)
# Runtime: 64 ms, faster than 39.08% of Python3 online submissions for Baseball Game.
# Memory Usage: 14.2 MB, less than 34.49% of Python3 online submissions for Baseball Game.

ops = ["5","2","C","D","+"]
print(calPoints(ops)) # 30
ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops)) # 27
ops = ["1"]
print(calPoints(ops)) # 1
