from typing import List
from collections import Counter
"""
backtracking
use counter to prevent duplicates
time: N!/(N-k)! combinations
    each comb * n recursion * n copy
    
space: O(N) for counter and comb
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                result.append(list(comb))
            
            # loop unique nums using counter
            for n in counter:
                if counter[n] > 0:
                    comb.append(n)
                    counter[n] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[n] += 1
        
        result = []
        cnt = Counter(nums)
        backtrack([], cnt)
        return result

"""
DFS
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(choices, comb):
            if len(choices) == 0:
                result.append(comb)
                return
            
            for i in range(len(choices)):
                if i > 0 and choices[i] == choices[i-1]:
                    continue
                dfs(choices[:i]+choices[i+1:], comb + [choices[i]])
        result = []
        nums.sort()
        dfs(nums, [])
        return result

s = Solution()
print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([1,2,3]))
print(s.permuteUnique([2,2,1,1]))
print(s.permuteUnique([3,3,0,3]))
        
