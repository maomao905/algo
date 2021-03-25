"""
allocate the more than 1 freq to free space

O(N)
"""
from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        cnt = Counter(cnt.values())
        
        ans = 0
        stack = []
        for freq in range(max(cnt.keys())+1):
            if cnt[freq] == 0:
                stack.append(freq)
            elif cnt[freq] > 1:
                while cnt[freq] > 1:
                    if stack:
                        ans += freq - stack.pop()
                    else:
                        ans += freq
                    
                    cnt[freq] -= 1
        return ans

s = Solution()
print(s.minDeletions('aab'))
print(s.minDeletions('aaabbbcc'))
print(s.minDeletions('ceabaacb'))
                
