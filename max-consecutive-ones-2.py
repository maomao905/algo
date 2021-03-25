from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero = 0
        
        N=len(nums)
        l=0
        ans = 0
        for r in range(N):
            if nums[r] == 0:
                zero += 1
            
            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        return ans

s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0]))
print(s.findMaxConsecutiveOnes([1,0,0,1,0,1]))
