"""
sliding window

expand the window until the condition is satisfied
once it's satisfied, we add count of length between right pointer and the end character
then shrink the window and repeat the process
"""

from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N=len(s)
        cnt = Counter()
        ans = 0
        r = 0
        for l in range(N):
            while not all(cnt[char] > 0 for char in 'abc'):
                if r >= N:
                    return ans
                cnt[s[r]] += 1
                r += 1
            # print(l,r,N-r+1,valid(cnt), cnt)
            ans += N-r+1
            cnt[s[l]] -= 1
        return ans

s = Solution()
print(s.numberOfSubstrings('abcabc'))
print(s.numberOfSubstrings('aaacb'))
print(s.numberOfSubstrings('abc'))
