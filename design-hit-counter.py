"""
deque
[(timestamp,count)]
[(2,1),(3,1),(300,1)] total = 3
timestamp of first hit in list
    - if first timestamp is older than current timestamp - 5mins, pop hit until all timestamp in list is within 5 mins
total hits
    - increment hits when new hit arrives
    - decrease hits when removing old hits from queue
"""
from collections import deque
from bisect import *
from threading import Lock
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = [[float('-inf'),0]] # (time, count)
        self.total = 0
        self.lock = Lock()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        with self.lock:
            if self.t[-1][0] == timestamp:
                self.t[-1][1] += 1
            else:
                c = self.t[-1][1]+1
                self.t.append([timestamp, c])
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        i = bisect(self.t, [timestamp-300, float('inf')])-1
        j = bisect(self.t, [timestamp,float('inf')])-1
        return self.t[j][1] - self.t[i][1]


# Your HitCounter object will be instantiated and called as such:
c = HitCounter()
c.hit(1)
c.hit(2)
c.hit(3)
print(c.getHits(4))
c.hit(300)
print(c.getHits(300))
print(c.getHits(301))
