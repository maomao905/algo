from typing import List
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        res = []
        for i in arr2:
            for _ in range(cnt[i]):
                res.append(i)
            del cnt[i]
        
        for i in sorted(cnt):
            for _ in range(cnt[i]):
                res.append(i)
        return res

s = Solution()
print(s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,9,2], arr2 = [2,1,4,3,9,6]))
