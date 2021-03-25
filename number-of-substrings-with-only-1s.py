class Solution:
    def numSub(self, s: str) -> int:
        N=len(s)
        ans = 0
        l = 0
        for r in range(N):
            if s[r] == '0':
                l = r+1
                continue
            
            ans += r-l+1
        
        return ans % (10**9+7)

class Solution:
    def numSub(self, s: str) -> int:
        return sum([(len(ones)+1) * len(ones) // 2 for ones in s.split('0')]) % (10**9+7)

s = Solution()
print(s.numSub('0110111'))
print(s.numSub('101'))
print(s.numSub('111111'))
print(s.numSub('000'))
            
            
