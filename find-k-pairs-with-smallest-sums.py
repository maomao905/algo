import heapq

"""
最初にnums1をk個min_heapに入れて、popしたらpopしたitemのnums2のindexを1つだけincrementしてpushする
time: O(KlogK)
space: O(K)
"""

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []
        
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        # O(KlogK)
        for i in range(len(nums1)):
            heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
            if len(min_heap) >= k:
                break
        
        ans = []
        
        # k loops * O(logK)
        while len(ans) < k:
            _, _i, _j = heapq.heappop(min_heap)
            ans.append([nums1[_i], nums2[_j]])
            
            if _j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[_i] + nums2[_j+1], _i, _j+1))
            
            # if k > N or k > M
            if _i == len(nums1)-1 and _j == len(nums2)-1:
                break
        
        return ans

s = Solution()
print(s.kSmallestPairs([1,7,11], [2,4,6], 3))
print(s.kSmallestPairs([1,7,11], [2,4,6], 10))
print(s.kSmallestPairs([1,7,11], [], 10))
print(s.kSmallestPairs([], [], 5))
        
        
