"""
(WA)
"""
from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N=len(nums)
        dp = [[0] * 3 for _ in range(N)]
        dp[0][nums[0]%3] = nums[0]
        ans = 0
        for i in range(1,N):
            mod = nums[i] % 3
            if mod == 0:
                dp[i][0] = dp[i-1][0] + nums[i]
                dp[i][1] = dp[i-1][1] + nums[i] if dp[i-1][1] else 0
                dp[i][2] = dp[i-1][2] + nums[i] if dp[i-1][2] else 0
            elif mod == 1:
                dp[i][0] = max(dp[i-1][2] + nums[i], dp[i-1][0]) if dp[i-1][2] else dp[i-1][0]
                dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1]) if dp[i-1][0] else dp[i-1][1]
                dp[i][2] = max(dp[i-1][1] + nums[i], dp[i-1][2]) if dp[i-1][1] else dp[i-1][2]
            else:
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i]) if dp[i-1][0] else dp[i-1][2]
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i]) if dp[i-1][1] else dp[i-1][0]
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i]) if dp[i-1][2] else dp[i-1][1]
            ans = max(ans, dp[i][0])
        return ans

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        N=len(nums)
        dp = [[float('-inf')] * 3 for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(1,N+1):
            mod = nums[i-1] % 3
            for j in range(3):
                m = (j+mod)%3
                dp[i][m] = max(dp[i-1][j] + nums[i-1], dp[i-1][m])
        return dp[-1][0]

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for n in nums:
            for s in dp[:]:
                mod = (s + n)%3
                dp[mod] = max(dp[mod], n+s)
        return dp[0]

s = Solution()
print(s.maxSumDivThree([3,6,5,1,8]))
print(s.maxSumDivThree([4]))
print(s.maxSumDivThree([1,2,3,4,4]))
print(s.maxSumDivThree([2,19,6,16,5,10,7,4,11,6]))
