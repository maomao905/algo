class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9+7

        ans = 0
        for i in range(1,n+1):
            ans <<= len(bin(i))-2
            ans = (ans + i) % MOD
        return ans
            
