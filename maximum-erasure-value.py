from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        seen = set()
        s = 0
        ans = 0
        l = 0
        for r in range(N):
            s += nums[r]
            while nums[r] in seen:
                seen.remove(nums[l])
                s -= nums[l]
                l += 1
            seen.add(nums[r])
            ans = max(ans, s)
        return ans

s = Solution()
print(s.maximumUniqueSubarray([4,2,4,5,6]))
print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
            
