"""
time: O(N+M)
space: O(N+M)
more precisely, distinct N + distinct M
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
        
s = Solution()
print(s.intersection([1,2,2,1], [2,2]))
