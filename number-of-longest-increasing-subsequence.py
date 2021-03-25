"""
DP
current num is larger than previous num, add it to subsequence because it's increasing
also add the count of subsequence from previous element
O(N^2) space O(N)
"""

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        dp = [1] * N # keep track of longest length ending at ith num
        cnt = [1] * N # keep track of count of longest subsequence ending at ith num
        
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    # new longest subsequence
                    if dp[j]+1 > dp[i]:
                        cnt[i] = cnt[j]
                        dp[i] = dp[j]+1
                    # another longest subsequence
                    elif dp[j]+1 == dp[i]:
                        cnt[i] += cnt[j]

        m = max(dp)
        return sum(cnt[i] for i in range(N) if dp[i] == m)

s = Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))
print(s.findNumberOfLIS([2,2,2,2,2]))
