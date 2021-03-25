"""
O(N)
"""

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N=len(nums)
        
        i = 1
        for n in range(nums[0]+1,nums[0]+k+N):
            if i < N and nums[i] == n:
                i += 1
                if i >= N:
                    return n + k
                continue
            
            k -= 1
            if k == 0:
                return n

"""
binary search
O(logN)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N=len(nums)
        l,r = 0, N-1
        
        while l < r:
            mid = l + sum(divmod(r-l,2))
            if nums[mid] - mid - nums[0] < k:
                l = mid
            else:
                r = mid-1
        
        k -= nums[l] - l - nums[0]
        return nums[l] + k
        


s = Solution()
print(s.missingElement([4,7,9,10], 1))
print(s.missingElement([4,7,9,10], 3))
print(s.missingElement([1,2,4], 3))
print(s.missingElement([1,2,3], 3))
