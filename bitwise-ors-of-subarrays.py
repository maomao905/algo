"""
OR subarray starting from 0th index to 2nd index
only 3 possibilities because once we have 1, all later elements become 1
0 0 1
0 1 1
1 1 1

arr = [1,2,4]

- subarray ending at 1
{1} = 01
- subarray ending at 2
{2} = 10
{1,2} = 11
- subarray ending at 4
{4} = 100
{2,4} = 110
{1,2,4} = 110

-> number of 1 bit is only increasing

O(32 * N) = 0(N)
"""
from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for i in arr:
            cur = {i|j for j in cur} | {i}
            res |= cur
        return len(res)

s = Solution()
print(s.subarrayBitwiseORs([1,2,4]))
