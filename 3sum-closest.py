"""
3sum -> sort O(NlogN) and two pointers O(N^2)
     -> N * hashset 2sum O(N) -> it cannot apply to this problem (closest)

sort O(NlogN) and two pointers O(N^2)
[-1,2,1,-4] -> sort [-4,-1,1,2]
-4 fixed  -1 + 2 = -3 < 1  left +1
          1 + 2 = -1 > 1    right -1 left==right x
          -> best is -1
-1 fixed   1 + 2 = 2 > 1 
          -> best is 2
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        best_remain = float('inf')
        for i in range(len(nums)):
            n = nums[i]
            
            left = i+1
            right = len(nums)-1
            
            remain = target - n
            while left < right:
                r = remain - nums[left] - nums[right]
                
                # exactly the same sum as target
                if r == 0:
                    return target
                elif r > 0:
                    left += 1
                else:
                    right -= 1
                
                if abs(r) < abs(best_remain):
                    best_remain = r
        
        return target - best_remain

s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
                
