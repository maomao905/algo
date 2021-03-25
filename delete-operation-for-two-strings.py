"""
every step, we have 4 choices
- delete char of word1
- delete char of word2
- delete char of word1 and word2
- delete nothing (when both chars are the same)

O(2^M * 2^N) without memorization
O(MN) with memorization
space O(MN)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N=len(word1),len(word2)
        memo = {}
        def helper(i,j):
            if i >= M or j >= N:
                return M-i + N-j
            
            if (i,j) not in memo:
                if word1[i] == word2[j]:
                    memo[i,j] = helper(i+1,j+1)
                else:
                    memo[i,j] = min(helper(i+1,j) + 1, helper(i,j+1) + 1)
            return memo[i,j]
        
        return helper(0,0)

"""
DP
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N=len(word1),len(word2)
        dp = [[0] * (N+1) for _ in range(M+1)]
        
        for i in range(0,M+1):
            for j in range(0,N+1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
                

s = Solution()
print(s.minDistance('sea', 'eat'))
print(s.minDistance('', ''))
