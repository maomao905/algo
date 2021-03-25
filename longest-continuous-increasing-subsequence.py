from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        ans = 1
        cur = 1
        N=len(nums)
        for i in range(1,N):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                cur = 1
            
            ans = max(ans, cur)
        return ans

s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([2,2,2,2]))
print(s.findLengthOfLCIS([3,2,1]))
print(s.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
