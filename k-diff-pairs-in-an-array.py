from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = set()
        seen = set()
        for n in nums:
            for i in ((n-k),(n+k)):
                if i in seen:
                    res.add(tuple(sorted([n,i])))
            seen.add(n)
        return len(res)

s = Solution()
print(s.findPairs([3,1,4,1,5],2))
print(s.findPairs([1,2,3,4,5],1))
print(s.findPairs([1,3,1,5,4],0))
print(s.findPairs([1,2,4,4,3,3,0,9,2,3],3))
print(s.findPairs([-1,-2,-3],1))
                
