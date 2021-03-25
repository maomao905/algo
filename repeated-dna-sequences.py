"""
substring match problem
brute-force
    1. check 10 letters -> then move next letter and check 10 letters
        - substring generation takes O(L)
    2. checked letters are saved in hashset
        - hash generation takes O(L)
    3. loop 1 and 2 until the end O(N)
    time: O((N-L)L) = O((N-10)10) = O(N)
    space: O((N-L)L) for hash set = O(N)
sliding window
    we can avoid substring generation by sliding the start and end only O(1)
rabin karp
    1. rolling hash takes O(1)
    2. check if hash appear before in hash set O(1)
    3. repeat this until the end O(N)
    time: O(N)
    space: O(N)
"""
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        W = 4
        if s == '':
            return []
        elif len(s) < L:
            return []
        d = {l: i for i, l in enumerate('ACGT')}
        hs = set()
        h = 0
        # hash function: 4 to the power of 10
        for i in range(L):
            h = W * h + d[s[i]]
        hs.add(h)
        ans = set()
        for i in range(1, len(s)-L+1):
            h -= d[s[i-1]] * (W ** (L-1))
            h *= W
            h += d[s[i+L-1]]
            if h in hs:
                ans.add(s[i:i+L])
            else:
                hs.add(h)
        return list(ans)

"""
bitmask

we can represent all letters in 2bits because we have only 4 letters

generate bit hash

when we shift, shift bit by 2
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        W = 4
        if s == '':
            return []
        elif len(s) < L:
            return []
        
        d = {l: i for i, l in enumerate('ACGT')}
        
        bitmask = 0
        seen = set()
        for i in range(L):
            bitmask <<= 2 # shift left by 2
            bitmask |= d[s[i]] # append new bits
        seen.add(bitmask)
        
        ans = set()
        for i in range(1, len(s)-L+1):
            bitmask <<= 2 # create space for new letter
            bitmask |= d[s[i+L-1]] # append new letter
            """
            >>> bin(3 << 2*10)
            '0b1100000000000000000000'
            >>> bin(~(3 << 2*10))
            '-0b1100000000000000000000' equals 0b0011111111111111111111
            bitmask & 0b0011111111111111111111
            -> first two bits become empty
            """
            bitmask &= ~(3 << 2 * L) # unset first two bits to 0
            if bitmask in seen:
                ans.add(s[i:i+L])
            else:
                seen.add(bitmask)
        return list(ans)

s = Solution()
print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(s.findRepeatedDnaSequences('AAAAAAAAAAAAA'))
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))
print(s.findRepeatedDnaSequences('A'))
