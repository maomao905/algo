"""
sliding window
keep track of how many distinct chars in the window
expand the window until num of distinct chars exeeds k

O(N)
"""
from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = 0
        N=len(s)
        r = 0
        for l in range(N):
            while len(cnt) <= k and r < N:
                cnt[s[r]] += 1
                if len(cnt) <= k:
                    ans = max(ans, r-l+1)
                
                r += 1
            
            cnt[s[l]] -= 1
            if cnt[s[l]] == 0:
                del cnt[s[l]]
        
        return ans

s = Solution()
print(s.lengthOfLongestSubstringKDistinct('eceba', 2))
print(s.lengthOfLongestSubstringKDistinct('aa', 1))
                
            
            
