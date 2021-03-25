"""
sliding window
two pointers
1. expand the window until condition is satisfied (move right pointer to right)
2. shrink the window as long as the condition stays satisfied (move left pointer to right)

we use two variables
- counter
    how many times the character needs to be included in the window
    if cnt[s] > 0, still s is missing
    if cnt[s] < 0, enough s is in the window and we can cut this character by shrinking the window
- missing
    how many characters needs to be included in the window
    when missing is zero, condition is fully satisfied
time O(N) space O(N)
"""
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        cnt = Counter(t)
        missing = len(t)
        l = r = L = R = 0
        for r, c in enumerate(s, 1):
            if cnt[c] > 0:
                missing -= 1
            cnt[c] -= 1
            
            if missing == 0:
                # now it's time to shrink the window but the window keeps satisfying the condition
                while l < r and cnt[s[l]] < 0:
                    cnt[s[l]] += 1
                    l += 1
                if R == 0 or R-L > r-l:
                    L,R = l,r
        return s[L:R]

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("aaaa", "aa"))
