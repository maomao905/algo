"""
[1,3],[2,6]

non-overlapping cases [1,2],[3,4] startA < startB, endA < endB, endA < startB
<---> <--->

overlapping cases
case1: [1,5],[2,3] startB < startA, endA < endB
    <---->
  <--------->
case2: [1,3],[2,5] startA < startB, endA < endB
  <--->
     <---->

1. sort by start time
2. if endA is greater than startB, merge.
prev = [1,3]
cur = [2,6] -> merge [prev start, max(prev end, cur end)] -> [1,6] update this as prev
cur = [8,10] 6 < 8, save prev in result

time: O(NlogN) space: O(N)
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = []
        for start, end in intervals:
            # merge
            if res and res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res

s = Solution()
print(s.merge([[1,6],[8,10],[15,18]]))
print(s.merge([[1,4],[4,5]]))
