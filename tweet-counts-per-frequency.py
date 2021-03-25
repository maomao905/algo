"""
recordTweet O(N)
getTweetCountsPerFrequency O(logN)
"""
from typing import List
from collections import defaultdict
from bisect import *
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 0
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        else:
            delta = 86400
        
        res = []
        j = bisect_left(self.tweets[tweetName], startTime)
        cur = startTime
        while cur <= endTime:
            i = bisect_right(self.tweets[tweetName], min(cur+delta-1, endTime))
            res.append(i-j)
            cur += delta
            j = i
        return res

# Your TweetCounts object will be instantiated and called as such:
obj = TweetCounts()
obj.recordTweet("3",60)
obj.recordTweet("3",120)
obj.recordTweet("3",70)
print(obj.getTweetCountsPerFrequency('minute', '3', 1, 119)) # 1-60, 61-120
print(obj.getTweetCountsPerFrequency('minute', '3', 0, 120))
obj.recordTweet("3",120)
print(obj.getTweetCountsPerFrequency('hour', '3', 1210000, 1210001))
