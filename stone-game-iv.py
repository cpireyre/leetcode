from array import array
from math import isqrt
from sys import argv
import functools

# you win if n is square when it's your turn
#print(316*316)
#print(317*317)
#squares = array('I', [x**2 for x in range(1, 316)])
#configurations = bytearray(n)
#moves = [x for x in squares if x <= 40]
#print (moves)
#print(configurations)
#print(squares)

# a configuration is one of:
# - winning, W, 1 in the byte array
# - losing, L, -1 in the byte array
# - ?, 0 in the byte array


#def canWin(n, configurations, squares):
#    if configurations[n] != 0:
#        return configurations[n]
#    else:
#        moves = (m for m in squares if m <= n)
#        for m in moves:
#            nextMove = n - m
#            if configurations[nextMove] == -1:
#                configurations[n] = 1
#                return 1
#            elif configurations[nextMove] == 0:
#                return canWin(nextMove, configurations, squares)
#        configurations[n] = -1
#        return -1
#
#n = int(argv[1])
#configurations = array('b', [0 for x in range(n + 1)])
#squares = array('I', [x**2 for x in range(isqrt(n), 0, -1)])
#for i in squares:
#    configurations[i] = 1
#print(squares)
#print(canWin(n, configurations, squares))

#print(squares)
#for i in squares:
#    configurations[i] = 1

#print(configurations)
#print(squares)
#print(canWin(n, configurations, squares))

#    else:
#        nextStates = [configurations[n - move] for move in
#                squares if move <= n]

#n = int(argv[1])
def canWin(n):
    S = {x**2 for x in range(1, isqrt(n) + 1)}

    if n in S:
        return True

    W = set(S)
    L = set()

    for i in range(1, n + 1):
        if i in W:
            continue
        Mgen = (m for m in S if m <= i and i - m in L)
        if any(Mgen):
            W |= {i}
        else:
            L |= {i}
    return n in W

@functools.cache
def canWinMemo(n):
    if not n: return False
    
    for i in reversed(range(1, isqrt(n) + 1)):
        if not canWinMemo(n - i**2): return True

    return False

ret = canWinMemo(int(argv[1]))
print(ret)

# if ANY move turns a ? into an L, then that ? is a W
# if ALL moves turn a ? into a W then the ? is an L
# if a move turns a ? into another ?, recur
