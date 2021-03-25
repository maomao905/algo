"""
first split choices * second split choices
"""
class Solution:
    def numWays(self, s: str) -> int:
        MOD=10**9+7
        N=len(s)
        if N<3:
            return 0
        
        ones = list(s).count('1')
        if ones == 0:
            return (N-1)*(N-2)//2 % MOD
        
        if ones % 3:
            return 0
        
        cnt = ones//3
        pos = [i for i, n in enumerate(s) if n == '1']
        
        l,r = pos[cnt]-pos[cnt-1], pos[-cnt]-pos[-cnt-1]
        return l*r % MOD

s = Solution()
print(s.numWays('10101'))
print(s.numWays('1001'))
print(s.numWays('0000'))
print(s.numWays('100100010100110'))
        
            
            
