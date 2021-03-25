"""
[1,2,3] k=2

brute-force
shift all elements one by one k times
O(NK)
1,2,3
3,1,2
2,3,1

shift all elements by k at one time
1,2,3
2,3,1
nums[i] = nums[i-k]
3 nums[2] = nums[2-2] = nums[0] = 1
2 nums[1] = nums[1-2] = nums[-1] = 3
1 nums[0] = nums[0-2] = nums[-2] = 2
if we shift from backward, we don't lose the previous element value

1,2,3
2,3,1

repeat to move to where it should be
change 3 to 1
change 2 to 3
change 1 to 2

O(N)
"""

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt = 0
        start = 0
        k %= len(nums)
        while cnt < len(nums):
            before = start
            prev = nums[start]
            while True:
                after = (before + k) % len(nums)
                nums[after], prev = prev, nums[after]
                before = after
                cnt += 1
                
                if before == start:
                    break
            start += 1
        print(nums)

s = Solution()
print(s.rotate(nums = [1,2,3,4,5,6,7], k = 3))
print(s.rotate(nums = [-1,-100,3,99], k = 2))
print(s.rotate(nums = [1,2,3,4,5,6], k = 3))
