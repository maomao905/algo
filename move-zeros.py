from typing import List

# time O(n)
# space O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt = nums.count(0)
        if cnt == 0:
            return nums
        
        zero_start_index = len(nums) - cnt
        
        i = 0
        j = 0
        
        while j < zero_start_index and i < len(nums):
            if nums[i] != 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j += 1
            i += 1
            print(nums, i, j, zero_start_index)
        # 
        # for idx in range(zero_start_index, len(nums)):
        #     nums[idx] = 0
        
        return nums

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
print(s.moveZeroes([1,0,1]))
        
