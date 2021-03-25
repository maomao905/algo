"""
3 sum's extension
time: O(N^3)
two sum takes O(N)
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def next_low_pos(l):
            l += 1
            while l < N and nums[l] == nums[l-1]:
                l += 1
            return l
        
        def next_high_pos(h):
            h -= 1
            while 0 <= h and nums[h] == nums[h+1]:
                h -= 1
            return h
        
        res = []
        N=len(nums)
        nums.sort()
        for i in range(N):
            _n = nums[i]
            if i-1 >= 0 and _n == nums[i-1]:
                continue
            for j in range(i+1, N):
                n = nums[j]
                if j-1 >= i+1 and n == nums[j-1]:
                    continue
                l, r = j+1, N-1
                _target = target - _n - n
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == _target:
                        res.append([_n, n, nums[l], nums[r]])
                        # print([_n, n, nums[l], nums[r]], i, j, l, r)
                        l = next_low_pos(l)
                        r = next_high_pos(r)
                    elif  sum <= _target:
                        l += 1
                    else:
                        r -= 1
        return list(res)
    

s = Solution()
print(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(s.fourSum(nums = [0,0,0,0], target = 0))
print(s.fourSum(nums = [-2,-1,-1,1,1,2,2], target = 0))
                
