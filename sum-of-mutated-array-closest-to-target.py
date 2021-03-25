"""
[1,10,9] target = 9 ans = 4 sum - target = 20 - 9 = 11, minimize the difference by reducing the large numbers
[1,10,9] target = 20 ans = 10 if sum is the same as target, maximum num is the answer
[1,10,9] target = 30 ans = 10 we can only reduce the sum of the array, maximum num is the answer

[1,1,1,1,10] target = 6 ans = 1
[1,1,1,1,10] target = 3 ans = 1
[1,10,10,10] target = 3 ans = 1
[1,1,10,10,100,100] target = 20 ans = 4

binary search
search best value between 0 and maximum value
if the sum with the value is too big, decrease the value
if the sum with the value is too small, increase the value


O(Nlog(maximum value))
"""
from typing import List
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        N=len(arr)
        ans = 0
        min_diff = float('inf')
        l, r = 0, max(arr)
        while l<=r:
            mid = (l+r)//2
            s = sum([min(n, mid) for n in arr])
            diff = s - target
            if abs(diff) < min_diff or (abs(diff) == min_diff and ans > mid):
                min_diff = abs(diff)
                ans = mid
            if diff == 0:
                return mid
            elif diff < 0:
                l = mid + 1
            else:
                r = mid - 1
        return ans

s = Solution()
print(s.findBestValue([4,9,3],10))
print(s.findBestValue([2,3,5],10))
print(s.findBestValue([60864,25176,27249,21296,20204], 56803))
        
