from typing import List
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        j = 0
        N=len(nums)
        for i in range(N-k+1):
            if nums[i] > nums[j]:
                j = i
        
        return nums[j:j+k]

"""
follow up (in case of duplicates)

two pointers
{4,3,4,3,4,3,5}, k = 5
         ^   ^
move pointer by d if nums[i] == nums[j] is the same
"""
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        j = 0
        d = 0
        for i in range(1,N):
            if nums[j+d] == nums[i] and d < k-1:
                d += 1
                continue
            
            if nums[j+d] < nums[i] and i-d+k-1<N:
                j = i-d
                
            d = 0
        
        return nums[j:j+k]
            
s = Solution()
print(s.largestSubarray([1,4,5,2,3],3))
print(s.largestSubarray([1,4,5,2,3],4))
print(s.largestSubarray([1,4,5,2,3],1))
        
