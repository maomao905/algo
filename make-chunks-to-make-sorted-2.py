"""
1. sort
2. keep max and compare the current element with sorted array

O(NlogN)
"""
from typing import List
from collections import Counter
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        
        cnt = Counter()
        ans = 0
        for n1, n2 in zip(arr, sorted_arr):
            cnt[n1] -= 1
            cnt[n2] += 1
            if cnt[n1] == 0:
                del cnt[n1]
            if cnt[n2] == 0:
                del cnt[n2]
            if len(cnt) == 0:
                ans += 1
        return ans

"""
    2,1,3,4,4
max 2,2,3,4,4 max from the head
min 1,1,3,4,4 min from the end

if max[i] <= min[i+1], ans += 1
"""
from itertools import accumulate
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N=len(arr)
        mx = list(accumulate(arr, max))
        mi = list(reversed(list(accumulate(reversed(arr), min))))
        ans = 0
        for i in range(N):
            if i+1 >= N or mx[i] <= mi[i+1]:
                ans += 1
        return ans

s = Solution()
print(s.maxChunksToSorted([5,4,3,2,1]))
print(s.maxChunksToSorted([2,1,3,4,4]))
print(s.maxChunksToSorted([2,1,2,4,1,2]))
                           # 1,1,2,2,2,4
