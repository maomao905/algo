class UndergroundSystem:

    def __init__(self):
        self.riding = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.riding[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        route = (self.riding[id][0], stationName)
        time = t - self.riding[id][1]
        if route not in self.time:
            self.time[route] = [time, 1]
        else:
            self.time[route][0] += time
            self.time[route][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        t, n = self.time[route]
        return t/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
