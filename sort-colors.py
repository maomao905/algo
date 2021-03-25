"""
[2,0,2,1,1,0]

0 is left-most and 2 is right-most
move the middle of 0 to left and move the middle of 2 to right 
"""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p_0 = -1
        for i in range(N):
            if nums[i] != 0:
                break
            p_0 += 1
        
        p_2 = len(nums)
        for i in reversed(range(N)):
            if nums[i] != 2:
                break
            p_2 -= 1
        # print(p_0,p_2)
        cur = p_0 + 1
        while cur < p_2:
            if nums[cur] == 0 and cur != p_0:
                nums[p_0+1], nums[cur] = 0, nums[p_0+1]
                p_0 += 1
            elif nums[cur] == 2 and cur != p_2:
                nums[p_2-1], nums[cur] = 2, nums[p_2-1]
                p_2 -= 1
            else:
                cur += 1
            # print(nums, p_0,p_2,cur)

s = Solution()
s.sortColors([2,0,2,1,1,0])
s.sortColors([1,2,0])
