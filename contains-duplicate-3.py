"""
(TLE)
O(nklogk)
"""
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N=len(nums)
        for i in range(N):
            window = sorted(nums[i:i+k+1])
            for i in range(1,len(window)):
                if window[i] - window[i-1] <= t:
                    return True
        return False

"""
(TLE)
brute force
compare current number with all numbers inside the k window
O(nk)
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N=len(nums)
        for i in range(N):
            for j in range(max(0,i-k),i):
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False

"""
(WA)
insertion/deletion costs O(N)
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N=len(nums)
        if N<2:
            return False
        if k == 0:
            return True
        
        window = []
        for i in range(max(N-k,1)):
            if i == 0:
                window = sorted(nums[i:i+k+1])
                for i in range(1,len(window)):
                    if window[i] - window[i-1] <= t:
                        return True
            else:
                window.remove(nums[i-1])
                n = nums[i+k]
                l,r = 0,k-1
                while l<r:
                    mid = (l+r)//2 + (r-l)%2
                    if window[mid] <= n:
                        l = mid
                    else:
                        r = mid - 1
                # print(window, l)
                if (window[l]<=n and n-window[l] <= t) or (l+1 < len(window) and window[l+1]-n <= t):
                    # print('-', window[l], n, window[l+1], l, 'i=',i, window)
                    return True
                window.insert(l+1, n)
        return False

"""
bucket

t size bucket

allocate each number into bucket
current number's bucket is j
if there is a number in (j-1,j,j+1) and difference is within t, return True
each bucket has at most 1 element because if multiple elements exists, it should be true already

O(N)
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        N=len(nums)
        if N==0:
            return False
        _min, _max = min(nums), max(nums)
        bucket_size = min(((_max - _min)//(t+1)) + 1, len(nums))
        buckets = [None] * bucket_size
        for i in range(N):
            j = min((nums[i]-_min)//(t+1), bucket_size-1)
            for _j in (max(0,j-1),j,min(j+1,bucket_size-1)):
                if buckets[_j]:
                    _n, _i = buckets[_j]
                    if abs(_i - i) <= k:
                        if abs(nums[i] - _n) <= t:
                            return True
                    else:
                        buckets[_j] = None
            buckets[j] = (nums[i], i)
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([1,2,3,1],3,0))
print(s.containsNearbyAlmostDuplicate([1,0,1,1],1,2))
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))
print(s.containsNearbyAlmostDuplicate([1],1,1))
print(s.containsNearbyAlmostDuplicate([-2147483648,2147483647],1,1))
print(s.containsNearbyAlmostDuplicate([2147483646,2147483647],3,3))
print(s.containsNearbyAlmostDuplicate([1,2],0,1))
            
                
        
