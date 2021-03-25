"""
brute-force
try all patterns

k cards from left ~ k cards from right
sliding window

O(K)
"""

from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = k-1
        right = 0
        
        cur_sum = sum(cardPoints[:k])
        max_sum = cur_sum
        
        for i in range(k):
            left_sub = cardPoints[left-i]
            right_add = cardPoints[-i-1]
            # print(left_sub, right_add)
            cur_sum = cur_sum - left_sub + right_add
            max_sum = max(cur_sum, max_sum)
        
        return max_sum

s = Solution()
print(s.maxScore([1,2,3,4,5,6,1], 3))
print(s.maxScore([2,2,2], 2))
print(s.maxScore([9,7,7,9,7,7,9], 7))
print(s.maxScore([1,1000,1], 1))
print(s.maxScore([1,79,80,1,1,1,200,1], 3))
