"""
brute-force
prev < current -> include or skip
prev >= current -> skip
time: O(2^n)
space: O(2^n)
"""
from typing import List
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         return self.recursive(nums, 0, float('-inf'))
# 
#     def recursive(self, nums, cur_pos, prev):
#         if cur_pos >= len(nums):
#             return 0
#         l1 = 0
#         if nums[cur_pos] > prev:
#             l1 = 1 + self.recursive(nums, cur_pos+1, nums[cur_pos])
# 
#         l2 = self.recursive(nums, cur_pos+1, prev)
#         return max(l1,l2)
"""
recursive with memorization
time: O(n^2) cur_posとprevの組み合わせの数だけあるのでn * n
space: O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.recursive(nums, 0, float('-inf'))

    def recursive(self, nums, cur_pos, prev, memo={}):
        if cur_pos >= len(nums):
            return 0

        if (cur_pos, prev) in memo:
            return memo[(cur_pos, prev)]
        l1 = 0
        if nums[cur_pos] > prev:
            l1 = 1 + self.recursive(nums, cur_pos+1, nums[cur_pos], memo)

        l2 = self.recursive(nums, cur_pos+1, prev, memo)
        memo[(cur_pos, prev)] = max(l1,l2)
        return memo[(cur_pos, prev)]
"""
dynamic programming with bottom up approach
time: O(n^2)
space: O(n) single array
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # i is current index
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)

"""
greedy

patience sorting
keep track of the minimum value in each pile
if new number is greater than min[-1], we create new pile,
otherwise, we put it into piple where it has the closest larger value

each pile forms decreasing order
[10, 9, 2, 5, 3, 7]
10  5  7  101  -> length is 4, which is the answer
9   3  18
2

[0,1,0,3,2,3]
0 1 3 3  -> length is 4
0   2

O(NlogN)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums)
        piles = [nums[0]]
        
        for n in nums[1:]:
            l,r = 0,len(piles)
            while l < r:
                mid = l+(r-l)//2
                
                if piles[mid] < n:
                    l = mid + 1
                else:
                    r = mid
            
            # print(l, len(piles)-1)
            if l == len(piles):
                piles.append(n)
            else:
                piles[l] = n
        
        return len(piles)


s = Solution()
# print(s.lengthOfLIS([0]))
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([7,7,7,7]))
print(s.lengthOfLIS([7]))
print(s.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
# print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
        
