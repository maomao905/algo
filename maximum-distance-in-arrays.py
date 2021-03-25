"""
M:arrays.length
N:aveage num of elements in a array

O(MNlogM)
"""
from heapq import *
from typing import List
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap = [(a[0],i,0) for i, a in enumerate(arrays)]
        max_heap = [(-a[-1],i,len(a)-1) for i, a in enumerate(arrays)]
        
        heapify(min_heap)
        heapify(max_heap)
        mi, mx = heappop(min_heap), heappop(max_heap)
        
        while mi[0] <= -mx[0]:
            if mi[1] != mx[1]:
                return -mx[0] - mi[0]
            if -mx[0] - min_heap[0][0] > -max_heap[0][0] - mi[0]:
                mi = heappop(min_heap)
                if mi[2] + 1 < len(arrays[mi[1]]):
                    heappush(min_heap, (arrays[mi[1]][mi[2]+1],mi[1],mi[2]+1))
            else:
                mx = heappop(max_heap)
                if mx[2] - 1 >= 0:
                    heappush(max_heap, (-arrays[mx[1]][mx[2]-1],mx[1],mx[2]-1))

"""
iterate and keep min and max

O(N)
"""    
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi,mx = arrays[0][0], arrays[0][-1]
        ans = 0
        for arr in arrays[1:]:
            ans = max(ans, abs(mx - arr[0]), abs(arr[-1] - mi))
            mi = min(arr[0], mi)
            mx = max(arr[-1], mx)
        return ans

s = Solution()
print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))
print(s.maxDistance([[1],[1]]))
print(s.maxDistance([[1],[2]]))
print(s.maxDistance([[1,4],[0,5]]))
print(s.maxDistance([[1,2],[1,2]]))
print(s.maxDistance([[1,4,4,4],[2,3,4,4]]))
print(s.maxDistance([[1,5],[3,4]]))
print(s.maxDistance([[-1,1],[-3,1,4],[-2,-1,0,2]]))
