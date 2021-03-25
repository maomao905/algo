from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        list(res.extend([k] * c) for k, c in (Counter(nums1) & Counter(nums2)).items())
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

s = Solution()
print(s.intersect([1,2,2,1],[2,2]))
print(s.intersect([4,9,5],[9,4,9,8,4]))
