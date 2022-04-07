from heapq import *

def lastStoneWeight(stones):
    stones = [-stone for stone in stones]
    heapify(stones)
    while len(stones) > 1:
        x, y = heappop(stones), heappop(stones)
        new = y - x if x > y else x - y
        if new:
            heappush(stones, new)
    return -heappop(stones) if len(stones) == 1 else 0
# Runtime: 39 ms, faster than 68.41% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14 MB, less than 17.07% of Python3 online submissions for Last Stone Weight

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones)) # 1
stones = [1]
print(lastStoneWeight(stones)) # 1
stones = [2, 2]
print(lastStoneWeight(stones)) # 0
