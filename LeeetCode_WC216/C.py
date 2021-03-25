"""
from backward
even sum, odd sum

even or odd turn
substruct last index of the turn

even done, odd done
"""
from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even, odd = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even_sum, odd_sum = sum(even), sum(odd)
        even_turn = (len(nums) + 1) % 2 == 0
        
        nums.reverse()
        
        even_done, odd_done = 0, 0
        
        # print(even_sum, odd_sum)
        fair = 0
        for n in nums:
            if even_turn:
                even_sum -= n
            else:
                odd_sum -= n
            
            # print((even_sum + even_done), (odd_sum + odd_done))
            if (even_sum + even_done) == (odd_sum + odd_done):
                fair += 1
            
            if even_turn:
                odd_done += n
            else:
                even_done += n
            
            even_turn = not even_turn
        
        return fair

s = Solution()
print(s.waysToMakeFair([2,1,6,4]))
print(s.waysToMakeFair([1,1,1]))
print(s.waysToMakeFair([1,2,3]))
                
        
