from itertools import accumulate


def canJump(ns):
    goal = len(ns) - 1

    def step(a, b):
        return b if b >= a - 1 else a - 1

    for station, fuel in enumerate(accumulate(ns, step)):
        if station + fuel >= goal:
            return True
        elif fuel <= 0:
            return False
# Runtime: 741 ms, faster than 38.34% of Python3 online submissions for Jump Game.
# Memory Usage: 15.1 MB, less than 83.79% of Python3 online submissions for Jump Game.



ns = [2, 3, 1, 1, 4]  # True
print(canJump(ns))
ns = [3, 2, 1, 0, 4]  # False
print(canJump(ns))
ns = [0]  # True
print(canJump(ns))
