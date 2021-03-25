"""
if w1[i] == w2[j]:
    count up
else:
    move i next or move j next

memorization
time O(MN) space O(MN)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N=len(text1),len(text2)
        memo = {}
        
        def helper(i,j):
            if i>=M or j>=N:
                return 0
            
            if (i,j) not in memo:
                if text1[i] == text2[j]:
                    memo[i,j] = helper(i+1,j+1) + 1
                else:
                    memo[i,j] = max(helper(i+1,j), helper(i,j+1))
            return memo[i,j]
        return helper(0,0)

"""
DP

time: O(MN)
space: O(MN)
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N=len(text1),len(text2)
        
        dp = [[0] * (N+1) for _ in range(M+1)]
        
        for i in range(1,M+1):
            for j in range(1,N+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

s = Solution()
# print(s.longestCommonSubsequence('abcde', 'ace'))
# print(s.longestCommonSubsequence('abc', 'abc'))
# print(s.longestCommonSubsequence('abc', 'def'))
print(s.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
print(s.longestCommonSubsequence("bb", "ab"))
