def eatPiles(piles, k):
    return sum(map(lambda a: -1 * (-a // k), piles))

def binarySearch(piles, h):
    lowerBound = 0
    upperBound = max(piles)
    while lowerBound + 1 < upperBound:
        k = (lowerBound + upperBound) // 2
        t = eatPiles(piles, k) 
        print("k=%d, l=%d, u=%d" % (k, lowerBound, upperBound))
        if t > h:
            lowerBound = k
        elif t <= h:
            upperBound = k
        print("k=%d, l=%d, u=%d" % (k, lowerBound, upperBound))
    return upperBound

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         if len(piles) == h:
#             return max(piles)
#         else:
#             return binarySearch(piles, h)

pile = [3, 6, 7, 11]
print(binarySearch(pile, 8))
print(binarySearch([30,11,23,4,20], 6))
print(binarySearch([30,11,23,4,20], 5))
print(binarySearch([312884470], 312884469))
print(binarySearch([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184], 823855818))
