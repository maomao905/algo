"""
3 variables
i: pointing nums1
j: pointing nums2
k: pointing inserting position of nums1

move i, j, k from backward
when i < 0 and j >= 0, push left nums2 into nums1
when i > 0 and j < 0, do nothing

if nums1[i] == nums2[j], move j pointer becauses nums1 should stay

time O(n+m) space O(1)
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i,j,k = m-1,n-1,len(nums1)-1
        
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            
            k -= 1
            # print(nums1, i, j, k)
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

s = Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)
s.merge([1,3,3,0,0,0],3,[3,5,6],3)
s.merge([1,3,3,0,0,0],3,[3,3,3],3)
s.merge([1],1,[],0)
                
        
