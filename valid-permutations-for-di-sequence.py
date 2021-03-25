"""
only focus on how many numbers are smaller or greater than current number
O(N^3)
"""
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        N=len(s)+1
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            dp[0][i] = 1
        # ith digit
        for i in range(1,N):
            choices = N-i
            # how many numbers left to choose
            # increase
            if s[i-1] == 'I':
                for j in range(choices):
                    # i-1 is smaller value
                    for k in range(j+1):
                        dp[i][j] += dp[i-1][k]
            # decrease
            else:
                for j in range(choices):
                    # i-1 is greater value
                    for k in range(j+1,choices+1):
                        dp[i][j] += dp[i-1][k]
        
        return sum(dp[-1])%(10**9 + 7)

"""
O(N^2)
"""
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        N=len(s)+1
        dp = [[0]*N for _ in range(N)]
        for i in range(N):
            dp[0][i] = 1
        # ith digit
        for i in range(1,N):
            choices = N-i
            # how many numbers left to choose
            # increase
            cur = 0
            if s[i-1] == 'I':
                for j in range(choices):
                    # i-1 is smaller value
                    cur += dp[i-1][j]
                    dp[i][j] = cur
            # decrease
            else:
                for j in reversed(range(choices)):
                    # i-1 is greater value
                    cur += dp[i-1][j+1]
                    dp[i][j] = cur
        return sum(dp[-1])%(10**9 + 7)

s = Solution()
print(s.numPermsDISequence('DID'))
