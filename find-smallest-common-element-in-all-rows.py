from typing import List

"""
O(MN)
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        remain = set(mat[0])
        for row in mat[1:]:
            remain &= set(row)
        
        if not remain:
            return -1
        
        return min(remain)
        
s = Solution()
print(s.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
