"""
brute-force O(n^2)
choose any [i,j] as start and end index

positive x positive = positive
negative x positive = negative
negative x negative = positive
0        x positive(negtive) = 0

if [i, j] index is maximum length,
nums[j] is positive product of [i..j-1] must be positive
nums[j] is negative product of [i..j-1] must be negative


dp[i] is maximum length of postive/negative subarray including ith index

if i == 0:
    dp[i][positive] = 1 if nums[i] > 0 else 0
    dp[i][negative] = 1 if nums[i] < 0 else 0

if num[i] is positive
    dp[i][positive] = dp[i-1][positive] + 1
    dp[i][negative] = dp[i-1][negative] + 1 if dp[i-1][negative] > 0 else 0
else if nums[i] is negative
    dp[i][positive] = dp[i-1][negative] + 1 if dp[i-1][negative] > 0 else 0
    dp[i][negative] = dp[i-1][positive] + 1
else if nums[i] is 0
    dp[i][negative] = 0
    dp[i][positive] = 0

[1,-2,-3,4]
postive   1 0 3 4  -> 4 is maximum
negative  0 2 1 2

[0,1,-2,-3,-4]
positive 0 1 0 3 2 -> 3 is maximum
negative 0 0 2 1 4

[-1,-2,-3,0,1]
positive 0 2 2 0 1 -> 2
negative 1 1 3 0 0

time: O(N), space: O(1)
"""

from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        prev_pos = prev_neg = 0
        
        max_len = 0
        for n in nums:
            cur_pos = cur_neg = 0
            if n > 0:
                cur_pos = prev_pos + 1
                cur_neg = prev_neg + 1 if prev_neg > 0 else 0
            elif n < 0:
                cur_pos = prev_neg + 1 if prev_neg > 0 else 0
                cur_neg = prev_pos + 1
            else:
                cur_pos = cur_neg = 0
            # print(cur_pos, cur_neg)
            max_len = max(max_len, cur_pos)
            prev_pos, prev_neg = cur_pos, cur_neg
        return max_len

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        N=len(nums)
        ans = 0
        cur = 1 # product up to ith index
        pos = neg = 0 # first positive/negative index, if 0, update pos = neg = -1
        for i in range(N):
            cur *= nums[i]
            if cur == 0:
                pos = neg = -1
                cur = 1
            elif cur > 0:
                if pos == -1:
                    pos = i
                ans = max(ans, i - pos + 1)
            else:
                if neg == -1:
                    neg = i
                ans = max(ans, i - neg)
        return ans
        
s = Solution()
print(s.getMaxLen([1,-2,-3,4]))
print(s.getMaxLen([0,1,-2,-3,-4]))
print(s.getMaxLen([-1,-2,-3,0,1]))
print(s.getMaxLen([-1,2]))
print(s.getMaxLen([1,2,3,5,-6,4,0,10]))
print(s.getMaxLen([]))
print(s.getMaxLen([-1000000000,-1000000000]))
            
