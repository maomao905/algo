from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max(cnt, key=cnt.get)

s = Solution()
print(s.majorityElement([3,2,3]))
