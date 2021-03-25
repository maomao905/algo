"""
1. check if it's palindrome O(N)
2. permute palindromes O(N!)
    - odd length
        - [any other chars][odd char][any other chars]
        - any other chars is all subset
            - to handle duplicates, use counter
            - abc
            - cab
            - bac
    - even length
        - [any other chars][any other chars]

time O((N/2)!) space O(N)
"""
from typing import List
from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def is_palindrome(s):
            cnt = Counter(s)
            return [char for char, c in cnt.items() if c%2], cnt
        
        def permute(cnt, comb=[]):
            if len(comb) == length:
                return [''.join(comb)]
            
            res = []
            for c in cnt:
                if cnt[c] > 0:
                    comb.append(c)
                    cnt[c] -= 1
                    res.extend(permute(cnt, comb))
                    comb.pop()
                    cnt[c] += 1
            return res
            
            
        
        odd_chars, cnt = is_palindrome(s)
        if len(odd_chars) > 1:
            return []
        if odd_chars:
            cnt[odd_chars[0]] -= 1
        cnt = Counter({char: c//2 for char, c in cnt.items() if c})
        length = sum(cnt.values())
        
        res = []
        odd_char = odd_chars[0] if odd_chars else ''
        for half in permute(cnt):
            res.append(half + odd_char + half[::-1])
        return res
            
        
s = Solution()
print(s.generatePalindromes('aabb'))
print(s.generatePalindromes('abc'))
print(s.generatePalindromes('accbcca'))
        
