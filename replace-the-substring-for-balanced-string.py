"""
sliding window

WWEQERQWQWWRWWERQWEQ
Counter({'W': 8, 'Q': 5, 'E': 4, 'R': 3}) -> should be all 5
we need to reduce W's count to 5, we need 3 W in the window

expand the window
when all needed strings are in the window, shrink the window
"""
from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        def valid(cnt, needed):
            for char, c in needed.items():
                if cnt.get(char, 0) < c:
                    return False
            return True
        
        N=len(s)
        n = N//4
        needed = Counter({char: cnt-n for char, cnt in Counter(s).items() if cnt > n})
        if not needed:
            return 0
        
        # print(needed)
        ans = float('inf')
        cnt = Counter()
        l = 0
        for r in range(N):
            cnt[s[r]] += 1
            while l <= r and valid(cnt, needed):
                ans = min(ans, r-l+1)
                cnt[s[l]] -= 1
                l += 1
        
        return ans
                
s = Solution()
print(s.balancedString('QWER'))
print(s.balancedString('QQWE'))
print(s.balancedString('QQQW'))
print(s.balancedString('QQQQ'))
print(s.balancedString('WWEQERQWQWWRWWERQWEQ'))
print(s.balancedString('WQWRQQQW'))
                
