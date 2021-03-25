"""
trie
O(N^2)
"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        N=len(S)
        ans = 0
        trie = {}
        for i in range(N):
            node = trie
            for j in range(i,N):
                if S[j] in node:
                    ans = max(j-i+1, ans)
                else:
                    node[S[j]] = {}
                node = node[S[j]]
        
        return ans

"""
binary search + rolling hash

O(NlogN)
"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        def exists(L):
            W, MOD = 26, 2**32
            WL = pow(W,L,MOD)
            h = 0
            seen = set()
            for i in range(N):
                if i < L:
                    h = (h * W + ord(S[i])) % MOD
                    if i == L-1:
                        seen.add(h)
                else:
                    h = (h * W - ord(S[i-L]) * WL + ord(S[i])) % MOD
                    if h in seen:
                        return True
                    seen.add(h)
            return False
            
        N=len(S)
        l,r = 0, N-1
        while l<r:
            mid = (l+r)//2 + (r-l)%2
            if exists(mid):
                l = mid
            else:
                r = mid - 1
        return l

s = Solution()
print(s.longestRepeatingSubstring('abcd'))
print(s.longestRepeatingSubstring('abbaba'))
print(s.longestRepeatingSubstring('aabcaabdaab'))
print(s.longestRepeatingSubstring('aaaaa'))
