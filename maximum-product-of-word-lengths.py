"""
O(26*N^2 + NL) NL is for buiding set N words * L length characters
"""

from typing import List
from collections import Counter
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        word_sets = [set(w) for w in words]
        N=len(words)
        for i in range(N):
            for j in range(i+1,N):
                if not(word_sets[i] & word_sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
                
        return ans

"""
bitmask
O(N^2 + NL)
"""
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        N=len(words)
        ws = [0] * N
        for i,w in enumerate(words):
            b = 0
            for c in w:
                b |= 1 << ord(c) - ord('a')
            ws[i] = b

        for i in range(N):
            for j in range(i+1,N):
                if not(ws[i] & ws[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans

s = Solution()
print(s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(s.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(s.maxProduct(["a","aa","aaa","aaaa"]))
