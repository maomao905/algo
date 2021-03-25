"""
backtracking

if we meet alphabet, we have two choices(lowercase, uppercase)
we recursively expading the result one by one

time: O(2^N*N) space: O(N) for recursion stack
"""

from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        N=len(S)
        res = []
        def helper(i, comb):
            if i == N:
                res.append(''.join(comb))
                return
            
            if S[i].isdigit():
                comb.append(S[i])
                helper(i+1, comb)
                comb.pop()
            else:
                for s in (S[i].lower(), S[i].upper()):
                    comb.append(s)
                    helper(i+1, comb)
                    comb.pop()
        helper(0, [])
        return res

s = Solution()
print(s.letterCasePermutation('a1b2'))
print(s.letterCasePermutation('3z4'))
print(s.letterCasePermutation('12345'))
print(s.letterCasePermutation('0'))
