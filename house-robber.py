"""
dynamic programming
f(k) = max(f(k-2)+K, f(k-1))

f(-1) = f(0) = 0 とする

[2,7,9,3,1]
f(1) = max(f(-1)+2, f(0)) = max(0+2, 0) = 2
f(2) = max(f(0)+7, f(1))  = max(0+7, 2) = 7
f(3) = max(f(1)+9, f(2))  = max(2+9, 7) = 11
f(4) = max(f(2)+3, f(3))  = max(7+3, 11) = 11
f(5) = max(f(3)+1, f(4))  = max(11+1,11) = 12

time: O(N)
space: O(1)
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        k_2 , k_1 = 0, 0
        max_amount = 0
        for n in nums:
            max_amount = max(k_2+n, k_1)
            k_2 = k_1
            k_1 = max_amount
        return max_amount

s = Solution()
print(s.rob([2,7,9,3,1]))
