def countEmptySpots(flowerbed) -> int:
    empties = 0
    for i in range(len(flowerbed)):
        prevPot = flowerbed[i - 1] if i > 0 else 0
        currPot = flowerbed[i]
        nextPot = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
        print([prevPot, currPot, nextPot])
        if not any([prevPot, currPot, nextPot]):
            flowerbed[i] = 1
            empties += 1
    return empties

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return True if countEmptySpots(flowerbed) >= n else False

print(countEmptySpots([1]))
print(countEmptySpots([0]))
print(countEmptySpots([1, 0, 0, 1]))
print(countEmptySpots([1, 0, 0, 0, 1]))
print(countEmptySpots([0, 0, 0, 0, 0]))
