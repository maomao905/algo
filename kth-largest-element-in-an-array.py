import heapq
from typing import List
"""
time: O(NlogK)
space: O(K)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            elif min_heap[0] < n:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)
        
        return min_heap[0]

"""
nlargest sort final result, thus last element is the kth largest
https://github.com/python/cpython/blob/master/Lib/heapq.py#L503-L519
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        

s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
