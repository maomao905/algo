"""
DP

if we know 'xx' is palindrome, if we know the left-most character(y) == right-most character(y),
the palindrome length increases by 2
yxxy

b b b a b

     b -> 1
    ab -> 1
   ba  -> 1
  bb   -> 2
 bb    -> 2
   bab -> 3 a is 1 and plus 2
  bba  -> 2 b != a but bb is 2
 bbb   -> 3 b is 1 and plus 2
  bbab -> 3 ba is 1 and plus 2
 bbba  -> 3 bb is 2 and b != a and max(bbb or bba) -> bbb is 3
 bbbab -> 4 bba is 2 and plus 2  ---> this is final result

dp[i][j] is longest palindromic subsequence length of s[i..j]
dp[i][j] = if s[i] == s[j], dp[i+1][j-1] + 2 else max(dp[i][j-1], dp[i+1][j])
  c b b d
c 1 1 2 2 -> upper-right is the answer      
b   1 2 2
b     1 1
d       1

why do we go backward for i?
dp[i+1][j-1] -> we refer i+1 and i+1 needs to be filled beforehand

time and space O(N^2)
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N=len(s)
        dp = [[1] * N for _ in range(N)]
        
        # go backward for i because we use i+1 for i
        for i in reversed(range(N)):
            # go forward for j because we use j-1 for j
            for j in range(N):
                if j-i < 2:
                    if s[i] == s[j]:
                        dp[i][j] = j-i+1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][N-1]

s = Solution()
print(s.longestPalindromeSubseq('bbbab'))
print(s.longestPalindromeSubseq('cbbd'))
