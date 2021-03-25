"""
brute force
O(N)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N=len(nums)
        if N==1:
            return 0
        ans = 0
        for i in range(N):
            if (i == 0 and nums[i] > nums[i+1]) or (i==N-1 and nums[i] > nums[i-1]) or (nums[i-1] < nums[i] > nums[i+1]):
                if nums[ans] < nums[i]:
                    ans = i
        return ans

"""
binary search
"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def is_peak(i):
            if i == 0:
                return nums[0] > nums[1]
            elif i == N-1:
                return nums[i] > nums[i-1]
            else:
                return nums[i-1] < nums[i] > nums[i+1]
            
        N=len(nums)
        if N==1:
            return 0
        
        l,r = 0,N-1
        while l<r:
            mid = l+(r-l)//2
            if is_peak(mid):
                return mid
            
            if mid + 1 < N and nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l

"""
binary search (simpler)
peak must exist in <= i nums[i] > nums[i+1]

O(logN)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N=len(nums)
        l,r = 0,N-1
        while l<r:
            mid = l+(r-l)//2
            if mid + 1 < N and nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l

s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1,2,3,4]))
print(s.findPeakElement([4,3,2,1]))
print(s.findPeakElement([2,1,2,1,2]))
            
