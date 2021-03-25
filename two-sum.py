from typing import List

"""
time and space O(N)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, n in enumerate(nums):
            remain = target - n
            if remain in seen:
                return [idx, seen[remain]]
            else:
                seen[n] = idx
        return []
        
s = Solution()
print(s.twoSum([3,3], 6))
print(s.twoSum([2, 7,11,15], 9))
