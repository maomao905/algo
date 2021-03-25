"""
sort and compare current and next element
O(NlogN)
"""
from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])
        return res

s = Solution()
print(s.minimumAbsDifference([4,2,1,3]))
