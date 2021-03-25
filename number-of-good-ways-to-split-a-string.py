from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        l = Counter()
        r = Counter(s)
        
        N=len(s)
        
        ans = 0
        for i in range(N-1):
            l[s[i]] += 1
            r[s[i]] -= 1
            if r[s[i]] == 0:
                del r[s[i]]
            if len(l) == len(r):
                ans += 1
        return ans

s = Solution()
print(s.numSplits('aacaba'))
print(s.numSplits('abcd'))
print(s.numSplits('aaaaa'))
print(s.numSplits('acbadbaada'))
