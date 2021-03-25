"""
s = 'cbaebabacd'
p = 'abc'

brute-force
1. find p's all anagrams O(P!)
    -> make trie
    -> we don't need to make all anagrams, instead, alphabet index O(P)
2. get all combinations of s O(2^S)
    -> iterate from the head and if it hits the trie, save the start index
    -> check same alphabet index O(26) = O(1) of P length O(P)
        -> O(PS)
    cba
     bae
    -> only first and last characters are different -> update only 2 O(1)
        -> O(S) * O(26) = O(S)
    -> overall O(P+S), and space O(26) = O(1)
    
3. choose the matched combination and return the start index
"""
from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        
        cur_c = Counter(s[:len(p)])
        res = []
        for i in range(len(s)-len(p)+1):
            # print(c, cur_c)
            if c == cur_c:
                res.append(i)
            cur_c[s[i]] -= 1
            if cur_c[s[i]] == 0:
                del cur_c[s[i]]
            if i+len(p) < len(s):
                cur_c[s[i+len(p)]] += 1
        
        return res

s = Solution()
print(s.findAnagrams('cbaebabacd', 'abc'))
print(s.findAnagrams('abab', 'ab'))
        
