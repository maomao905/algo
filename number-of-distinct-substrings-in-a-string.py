"""
trie

O(N^2)
"""

class Solution:
    def countDistinct(self, s: str) -> int:
        trie = {}
        
        N=len(s)
        ans = 0
        for i in range(N):
            node = trie
            for j in range(i, N):
                if s[j] not in node:
                    ans += 1
                    node[s[j]] = {}
                node = node[s[j]]
        
        return ans

s = Solution()
print(s.countDistinct('aabbaba'))
print(s.countDistinct('abcdefg'))
                
