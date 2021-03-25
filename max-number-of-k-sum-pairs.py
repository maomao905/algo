"""
hash map
time O(N)
space O(N)
"""

from typing import List
from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        for n in nums:
            t = k-n
            if cnt[t] > 0:
                cnt[t] -= 1
                ans += 1
            else:
                cnt[n] += 1
        return ans

s = Solution()
print(s.maxOperations([1,2,3,4],5))
print(s.maxOperations([3,1,3,4,3],6))
