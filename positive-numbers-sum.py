"""
k = 2 n-1 + n = 2n-1
k = 3 n-1 + n + n+1 = 3n
k = 4 n-2 + n-1 + n + n+1 = 4n-2
k = 5 n-2 + n-1 + n + n+1 + n+2 = 5n
k = 6 n-3 + n-2 + n-1 + n + n+1 + n+2 = 6n-3
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        k = 1
        while k < N:
            if k % 2:
                cnt += bool(N % k == 0)
            else:
                cnt += bool((N + k // 2) % k == 0)
            k += 1
        
        return cnt
            
