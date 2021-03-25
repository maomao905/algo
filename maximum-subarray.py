"""
time: O(N)
space: O(1)
Kadane's algorithm
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        current_sum = 0
        for n in nums:
            current_sum += n
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        
        return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([1]))
print(s.maxSubArray([0]))
print(s.maxSubArray([-1]))
print(s.maxSubArray([-2147483647]))

            
