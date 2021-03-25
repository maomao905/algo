"""
generate all combinations
-> recursion
-> memorization doesn't work since we generate all output eventually (result list copy requires O(N))

in order to avoid duplicates,
we need to sort to place duplicate nums next to each other,
and never start the same number again once visited

O(2^N) N: length of candidates space: O(N)
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursion(start, t, comb=[]):
            # goal
            if t == 0:
                res.append(list(comb))
                return
            
            # validate
            if t < 0 or start >= len(candidates):
                return
            
            for i in range(start, len(candidates)):
                # skip duplicates
                # we don't want to append the same number in the same position in comb
                if start < i and candidates[i] == candidates[i-1]:
                    continue
                
                comb.append(candidates[i])
                recursion(i+1, t-candidates[i], comb)
                # backtrack
                comb.pop()
        
        candidates.sort()
        res = []
        recursion(0, target)
        return res

s = Solution()
print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print(s.combinationSum2(candidates = [2,5,2,1,2], target = 5))
