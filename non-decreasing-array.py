""" 
   6              
  / \           3 - 3
 /   3  ->     /
2            2

  6
 / \           6 - 6
4   \  ->     /
     3      4     

1. make previous num smaller to current num
    - this should be prioritized since the maximum can be suppressed and easier to achieve non-decreasing order
    - it's possible when nums[i-2] <= nums[i]
2. make current num larger to previous num
    - this should be used when choice 1 is not possible
    - when nums[i-2] > nums[i]
"""
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N=len(nums)
        cnt = 0
        for i in range(1,N):
            if nums[i-1] <= nums[i]:
                continue
            
            cnt += 1
            if cnt > 1:
                return False
            
            if i-2 >= 0 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
        
        return True

s = Solution()
print(s.checkPossibility([4,2,3]))
print(s.checkPossibility([3,4,2,3]))
print(s.checkPossibility([4,2,1]))
