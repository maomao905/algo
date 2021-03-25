"""
merge intervals
O(NlogN)
"""
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        intervals = []
        N=len(arr)
        for i in range(N):
            intervals.append([min(i, arr[i]), max(i, arr[i])])
        
        res = []
        for s, e in sorted(intervals):
            if res and res[-1][1] > s:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
            
        return len(res)

"""
keep max and max == index, we can split

     [0, 2, 1, 4, 3, 5, 7, 6]
 max [0, 2, 2, 4, 4, 5, 7, 7]
      ^     ^     ^  ^     ^

O(N)
"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        intervals = []
        N=len(arr)
        
        ans = 0
        mx = -1
        for i in range(N):
            mx = max(mx, arr[i])
            if mx == i:
                ans += 1
        return ans

from itertools import accumulate
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum(i == n for i, n in enumerate(accumulate(arr, max)))

s = Solution()
print(s.maxChunksToSorted([4,3,2,1,0]))
print(s.maxChunksToSorted([1,0,2,3,4]))
