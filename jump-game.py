def canJump(ns):
    goal = len(ns) - 1
    fuel = -1
    for station, tank in enumerate(ns):
        fuel = tank if tank >= fuel - 1 else fuel - 1
        if station + fuel >= goal:
            return True
        elif fuel <= 0:
            return False
# Runtime: 492 ms, faster than 92.61% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 20.93% of Python3 online submissions for Jump Game.

ns = [2,3,1,1,4] # True
print(canJump(ns))
ns = [3,2,1,0,4] # False
print(canJump(ns))
ns = [0] # True
print(canJump(ns))
