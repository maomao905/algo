"""
monotonically decreasing order in deque
- why we use deque?
    - popleft oldest element to keep sliding window O(1)
    - pop the smaller element than current element to keep the decreasing order O(1)
- first element is always the largest element

nums = [1,3,-1,-3,5,3,6,7], k = 3
       [3,-1]  -> max 3
cur=-3 [3,-1]
       [3,-1,-3] -> max 3
cur=5  [-1,-3]
       [5] # remove all elements smaller than current one (5) -> max 5
cur=3  [5]
       [5,3] -> max 5
cur=6  [5,3]
       [6] -> max 6
cur=7  [6]
       [7] -> max 7

time: O(N)
space: O(k)
"""

from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        N=len(nums)
        res = []
        
        for i in range(N):
            # remove the old element, which is out of current window if it's maximum
            # we don't need to all old elements as long as the maximum element only matters
            while q and q[0] <= i - k:
                q.popleft()
            
            # remove all elements smaller than current element
            # becuase we only need to know the max of current window
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            if i >= k-1:
                res.append(nums[q[0]])
        
        return res

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(s.maxSlidingWindow(nums = [1,-1], k = 1))
            
            
