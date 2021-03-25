"""
Boyer Moore Voting Algorithm
more than n/3 times -> at most 2 items -> we need only 2 variables to keep track of majority candidates

increment the count of the candidate if the number == candidate
decrement the count of the candidate (paired out) if the number != candidate, 
if the count is zero, the current number becomes the candidate and increment the count by 1

finally, verify the candidates are actually majority (there may be no majority)

      [1,1,2,3,3,1]
cand1  1 1       1
cnt1   1 2       3
cand2      2 x 3
cnt2       1 0 1

time O(N) space O(1)
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        
        for n in nums:
            if n == cand1:
                cnt1 += 1
            elif n == cand2:
                cnt2 += 1
            elif cnt1 == 0: # we have a room to place n as a candidate
                cand1 = n
                cnt1 += 1
            elif cnt2 == 0: # we have a room to place n as a candidate
                cand2 = n
                cnt2 += 1
            else:
                cnt1 -= 1 # paired out by n
                cnt2 -= 1 # paired out by n
        
        N=len(nums)
        res = []
        threshold = N//3
        if nums.count(cand1) > threshold:
            res.append(cand1)
        if nums.count(cand2) > threshold:
            res.append(cand2)
        return res

s = Solution()
# print(s.majorityElement([3,2,3]))
# print(s.majorityElement([1]))
# print(s.majorityElement([1,2]))
# print(s.majorityElement([1,2,4,1,2,3,3,1]))
# print(s.majorityElement([]))
print(s.majorityElement([2,1,1,3,1,4,5,6]))
