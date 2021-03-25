from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(i, comb):
            if i == N:
                if len(comb) >= 2:
                    res.add(tuple(comb))
                return
            
            helper(i+1, comb)
            
            if not comb or comb[-1] <= nums[i]:
                comb.append(nums[i])
                helper(i+1, comb)
                comb.pop()
            
        
        N=len(nums)
        res = set()
        helper(0, [])
        return list(map(list, res))

"""
another way to skip duplicates
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(i, comb):
            if len(comb) >= 2:
                res.append(list(comb))
            
            if i == N:
                return
                
            seen = set()
            for j in range(i,N):
                if nums[j] not in seen and (not comb or comb[-1] <= nums[j]):
                    seen.add(nums[j])
                    comb.append(nums[j])
                    helper(j+1, comb)
                    comb.pop()
        
        N=len(nums)
        res = []
        helper(0, [])
        return res
        

s = Solution()
print(s.findSubsequences([4,6,7,7,7]))
