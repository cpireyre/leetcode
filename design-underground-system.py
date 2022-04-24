class UndergroundSystem:

    def __init__(self):
        self.trips = {}
        self.moving = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.moving.update({id: (stationName, t)})

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source, departure = self.moving.pop(id)
        if (source, stationName) not in self.trips:
            self.trips[(source, stationName)] = [t - departure]
        else:
            self.trips[(source, stationName)].append(t - departure)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.trips[(startStation, endStation)]) / len(self.trips[(startStation, endStation)])
# Runtime: 346 ms, faster than 37.35% of Python3 online submissions for Design Underground System.
# Memory Usage: 24.1 MB, less than 60.84% of Python3 online submissions for Design Underground System.
