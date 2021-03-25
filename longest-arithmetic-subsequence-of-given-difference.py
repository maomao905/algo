from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N=len(arr)
        dp = [1] * N
        seen = {}
        for i in range(N):
            sub = arr[i]-difference
            if sub in seen:
                dp[i] = dp[seen[sub]] + 1
            seen[arr[i]] = i
        return max(dp)

s = Solution()
print(s.longestSubsequence([1,2,3,4], 1))
print(s.longestSubsequence([1,3,5,7], 1))
print(s.longestSubsequence([1,4,7,8,5,3,4,2,1], -2))
