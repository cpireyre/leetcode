from itertools import cycle, islice

def enoughGas(gas, cost):
    return sum(gas) >= sum(cost)

def zipRoad(gas, cost):
    return [(x, gas[x], cost[x]) for x in range(0, len(gas))]

def printTup(roadTup):
    print("Index: %d, gas here: %d, cost->%d"
            % (roadTup[0], roadTup[1], roadTup[2]))

def printRoad(road):
    for k in road:
        printTup(k)

def possibleStartIndices(road):
    return [x[0] for x in road if x[1] >= x[2] and x[1] > 0]

def offsetRoad(road, offset):
    c = cycle(road)
    return list(islice(c, offset, offset + len(road)))

def canTravelRoad(road):
    gas = 0
    for x in road:
        gas += x[1]
        gas -= x[2]
        if gas < 0:
            return False
    return True

def findStartIfExists(road):
    candidates = possibleStartIndices(road)
    for c in candidates:
        currRoad = offsetRoad(road, c)
        if canTravelRoad(currRoad):
            return c
    return -1

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if not enoughGas(gas, cost):
            return -1
        else:
            return findStartIfExists(zipRoad(gas, cost))

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

#print(enoughGas(gas, cost))
#print(enoughGas([2,3,4], [3,4,3]))
road = zipRoad(gas, cost)
road2 = zipRoad([2,3,4], [3,4,3])
#printRoad(road)
#print(possibleStartIndices(road))
#print(road)
#print(offsetRoad(road, 3))
print(findStartIfExists(road))
print(findStartIfExists(road2))
