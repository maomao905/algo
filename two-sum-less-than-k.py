"""
binary search
O(NlogN)
"""
from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def binary_search(l, t):
            r = N-1
            while l<r:
                mid = (l+r)//2 + (r-l)%2
                if t > nums[mid]:
                    l = mid
                else:
                    r = mid-1
            return l
            
        N=len(nums)
        nums.sort()
        ans = -1
        for i in range(N-1):
            if k < nums[i]:
                break
            j = binary_search(i+1, k-nums[i])
            s = nums[i] + nums[j]
            if s < k and s > ans:
                ans = s
        return ans

"""
binary search using bisect
O(NlogN)
"""
from bisect import *
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        ans = -1
        for i in range(N-1):
            if k < nums[i]:
                break
            j = bisect_left(nums, k-nums[i],i+1)-1
            if i < j:
                ans = max(ans, nums[i]+nums[j])
        return ans

"""
two pointers
O(NlogN)
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        N=len(nums)
        nums.sort()
        i,j = 0,N-1
        ans = -1
        while i<j:
            s = nums[i]+nums[j]
            if s < k:
                i+=1
                ans = max(ans, s)
            else:
                j-=1
        return ans
            
s = Solution()
print(s.twoSumLessThanK([34,23,1,24,75,33,54,8],60))
print(s.twoSumLessThanK([10,20,30],15))
print(s.twoSumLessThanK([1,2,10,12],4))
print(s.twoSumLessThanK([499,451,631,986,937,847,540,697,502,12,166,633,536,603,316,645,182,976,79,404,893,749,823,753,428,943,868,755,223,904,205,541,407,308,829,751,703,156,529,67,785,422,691,905,928,706,594,203,548,662]
,1900))
