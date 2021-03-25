"""
(WA)
3 smallest and 3 largest elements may change

0. take 3 smallest and 3 largest elements
1. get the contribution when we change the number nums[i] - nums[i-1]
  choose the num which has higher contribution
2. answer is right - left

[9,48,92,48,81,31] this case does not work

O(N)
"""
from heapq import *
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def take_small(small, large, smallest, largest):
            s = smallest[-1][0] - small[0]
            l = large[0] - largest[-1][0]
            if s == l:
                for i in range(1,4):
                    if len(smallest) < i:
                        return False
                    elif len(largest) < i:
                        return True
                    elif smallest[-i][0] - small[0] > large[0] - largest[-i][0]:
                        return True
                return False
            return s > l
                        
            
        N=len(nums)
        if N<=4:
            return 0
        
        nums = [(n, i) for i, n in enumerate(nums)]
        smallest = list(reversed(nsmallest(4, nums)))
        largest = list(reversed(nlargest(4, nums)))
        small, large = smallest.pop(), largest.pop()
        for _ in range(3):
            # if index is the same, they are the same number, small and large meet, so returns here
            if small[1] == large[1]:
                return 0
                
            # if contribution is the same, loop at most 3 times to check which to choose
            if take_small(small, large, smallest, largest):
                small = smallest.pop()
            else:
                large = largest.pop()
        return large[0] - small[0]

"""
heap
check all 4 pairs
O(N)
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N=len(nums)
        if N<=4:
            return 0
        smallest = list(reversed(nsmallest(4, nums)))
        largest = list(nlargest(4, nums))
        
        ans = 2e9
        for s, l in zip(smallest, largest):
            ans = min(ans, l-s)
        return ans
                
s = Solution()
print(s.minDifference([5,3,2,4]))
print(s.minDifference([1,5,0,10,14]))
print(s.minDifference([6,6,0,1,1,4,6]))
print(s.minDifference([1,5,6,14,15]))
print(s.minDifference([9,48,92,48,81,31]))
        
