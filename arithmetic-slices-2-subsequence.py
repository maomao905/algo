"""
base case: initialize dp[i] = 0, start from i == 2
dp[j][k] = dp[i][j] + 1 where A[k]-A[j] == A[j]-A[i]

O(N^3)
"""
from typing import List
from collections import defaultdict, Counter
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N=len(A)
        if N < 3:
            return 0
        
        dp = [[0]*N for _ in range(N)]
        seen = defaultdict(list) # value: list of index
        ans = 0
        for k in range(N):
            for j in range(1,k):
                diff = A[k]-A[j]
                for i in seen[A[j] - diff]:
                    if i >= j:
                        break
                    dp[j][k] += dp[i][j] + 1
                ans += dp[j][k]
                
            seen[A[k]].append(k)
        
        return ans

"""
O(N^2) using counter hashmap

above solution increments valid i,j,k one by one
but we can keep counter of different for each index
"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        N=len(A)
        if N < 3:
            return 0
        ans = 0
        dp = defaultdict(Counter)
        for k in range(N):
            for j in range(k):
                diff = A[k] - A[j]
                dp[k][diff] += 1
                dp[k][diff] += dp[j][diff] # i <-diff-> j <-diff-> k
                ans += dp[j][diff] # increment count of valid i,j,k
        return ans
        
s = Solution()        
print(s.numberOfArithmeticSlices([2,4,6,8,10]))
