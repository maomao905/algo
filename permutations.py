from typing import List

"""
backtracking
nums = [1,2,3]

target_index = 0
i = 0 [1,2,3]
    fist = 1
        i = 1 swap(nums[1], nums[1]) [1,2,3]
        i = 2 swap(nums[1], nums[2]) [1,3,2]
i = 1 swap(nums[0], nums[1]) [2,1,3]
    target_index = 1
        i = 1 swap(nums[1], nums[1]) [2,1,3]
        i = 2 swap(nums[1], nums[2]) [2,3,1]
i = 2 swap(nums[0], nums[2]) [3,1,2]
    target_index = 1
        i = 1 swap(nums[1], nums[1]) [3,1,2]
        i = 2 swap(nums[1], nums[2]) [3,2,1]
time: each permuation takes n recursive calls O(N!) * O(N)
      each permuation copy the result list O(N)
      O(N! * N^2) but roughly O(N!)
        
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        def recursive(i):
            if i == N:
                res.append(list(nums))
            
            for j in range(i, N):
                nums[i], nums[j] = nums[j], nums[i]
                recursive(i+1)
                # backtrack
                nums[i], nums[j] = nums[j], nums[i]
                
        recursive(0)
        return res
    
s = Solution()
print(s.permute([1,2,3]))
                
