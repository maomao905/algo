"""
store maximum positive numbers and minimum negative products up to ith index (including i-th index)

     2   3   -2  4
p 0  2   6   0   4  --> 6 is maximum
n 0  0   0 -12 -48

     -2  0  -1
p 0  0   0  0
n 0 -2   0  -1

time: O(N)
space: O(1)
"""
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        N = len(nums)
        pos = [0] * N
        neg = [0] * N
        
        for i in range(N):
            n = nums[i]
            if i == 0:
                if n > 0:
                    pos[i] = n
                else:
                    neg[i] = n
            else:
                if n == 0:
                    pos[i] = neg[i] = 0
                elif n > 0:
                    pos[i] = max(pos[i-1] * n, n) # consider pos[i-1] == 0, then we should save n
                    neg[i] = neg[i-1] * n
                else:
                    pos[i] = neg[i-1] * n
                    neg[i] = min(pos[i-1] * n, n)
        
        return max(pos)

"""
simpler same approach
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            _max = n * max_so_far
            _min = n * min_so_far
            min_so_far = min(_max, _min, n)
            max_so_far = max(_max, _min, n)
            res = max(res, max_so_far)
        return res
        
s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([-2,0,-2]))
print(s.maxProduct([-2]))
print(s.maxProduct([7,-2,-4]))
