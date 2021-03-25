"""
on <---k off---> on

first time k consecutive bulbs off and surrounded by on bulbs

brute-force
every time, check if k consecutive bulbs off and surrounded by on bulbs
O(N^2)

balanced binary tree
x1   x3   x2
turn on x3 (insert x3) and check left and right if there is another on-bulb exactly k distance away

insert takes O(logN)
O(NlogN)
"""
from sortedcontainers import SortedList
from typing import List
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        sl = SortedList([float('-inf'), float('inf')])
        for day, n in enumerate(bulbs, 1):
            sl.add(n)
            i = sl.index(n)
            if k+1 in (sl[i] - sl[i-1], sl[i+1] - sl[i]):
                return day
        return -1

s = Solution()
print(s.kEmptySlots([1,3,2], 1))
print(s.kEmptySlots([1,2,3], 1))
