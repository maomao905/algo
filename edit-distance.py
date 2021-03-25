"""
replace | insert
---------
delete

1. insert
ab -> abd   i=1  m
bd ->  bd   j=0  n-1

2. delete
ab -> a     i=0  m-1
bd -> bd    j=1  n

3 replace
ab -> ad    i=0  m-1
bd -> bd    j=0  n-1

if s[i] != s[j]
    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
else:
    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
  
  '' r o s
'' 0 1 2 3 (only insert)
h  1 1 2 3
o  2 2 1 2
r  3 2 2 2
s  4 3 3 2
e  5 4 4 3 --> 3 is the answer

time O(MN) space O(MN)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N=len(word1),len(word2)
        
        dp = [[0] * (N+1) for _ in range(M+1)]
        
        for i in range(M+1):
            for j in range(N+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        return dp[-1][-1]

s = Solution()
print(s.minDistance('horse', 'ros'))
print(s.minDistance('intention', 'execution'))
print(s.minDistance('intention', ''))
print(s.minDistance("zoologicoarchaeologist", "zoogeologist"))
