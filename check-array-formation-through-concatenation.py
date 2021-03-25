"""
hashmap
{value: (index of outer list, index of inner list)}
when value matches, update value with next value

time O(N) space: O(N)
"""
from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        p = {pieces[i][0]: i for i in range(len(pieces))}
        
        cur = 0
        while cur < len(arr):
            if arr[cur] not in p:
                return False
            
            idx = p[arr[cur]]
            for n in pieces[idx]:
                if n != arr[cur]:
                    return False
                cur += 1
        
        return True

s = Solution()
print(s.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
print(s.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
print(s.canFormArray([1,2,3], [[2],[1,3]]))
        
