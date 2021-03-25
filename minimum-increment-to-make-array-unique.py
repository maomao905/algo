"""
maintain the maximum value that is at least needed
count maximum value - n at each iteration

O(NlogN)
"""
from typing import List

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        cur = float('-inf')
        ans = 0
        for n in A:
            if cur >= n:
                cur += 1
                ans += (cur-n)
            else:
                cur = n
        return ans

"""
Union-Find
"""
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        root = {}
        def find(x):
            root[x] = find(x + 1) if x in root else x
            return root[x]
        
        return sum(find(n) - n for n in A)
        

s = Solution()
print(s.minIncrementForUnique([1,2,2]))
print(s.minIncrementForUnique([3,2,1,2,1,7]))
            
