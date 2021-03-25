"""
binary search
error can be less than 1e-5 -> binary search

1. boundary of average
left = minimum value of the array
right = maximum value of the array
mid = (left+right)/mid

2. check the mid average is possible O(N)
- particular length of subarray average
(a1+a2+a3+...+aj)/j >= mid
 a1+a2+a3+...+aj >= mid * j
(a1-mid)+(a2-mid)+(a3-mid)+...+(aj-mid) >= 0

- use prev_sum, min_sum, cur_sum to find the maximum sum that is no less than mid
<----- cur_sum -----> cur_sum is just cumulative sum up to current index i
<--prev_sum--><--k--> prev_sum is previous cumulative sum up to i-k index
<-min_sum-><-maxsum-> min_sum is minimum sum among all prev_sum so far

cur_sum - min_sum is maximum average which is greater than mid
for example, if min_sum is negative, cur_sum - min_sum > cur_sum which maximize the average

O(NlogM) M:(max value - min value)
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(m):
            cur_sum = prev_sum = min_sum = 0
            arr = [n-m for n in nums]
            for i in range(N):
                cur_sum += arr[i]
                if i >= k-1:
                    if cur_sum - min_sum >= 0:
                        return True
                    
                    prev_sum += arr[i-k+1]
                    min_sum = min(min_sum, prev_sum)
                    
            return False
        
        N=len(nums)
        l,r = min(nums), max(nums)
        
        while r-l >= 1e-5:
            mid = (l+r)/2
            
            if check(mid):
                l = mid
            else:
                r = mid
        
        return l

s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3],4))
print(s.findMaxAverage([5],1))
print(s.findMaxAverage([0],1))
