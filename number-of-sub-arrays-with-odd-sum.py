"""
cumulative sum

if cum_sum is odd, add even cum_sum up to current index
 odd - even = odd (e.g. 7-2 = 5)
if cum_sum is even, add odd cum_sum up to current index
 even - odd = odd (e.g. 6 - 1 = 5)
 
 [1,3,5]
            1  3  5
odd_cnt   0 1  1  2
even_cnt  1 0  2  1
cnt         1  1  2 -> sum is 4

time O(N) space O(1)
"""

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_cnt, even_cnt = 0, 1
        is_odd = 0
        cnt = 0
        for n in arr:
            is_odd ^= n % 2
            if is_odd:
                cnt += even_cnt
                odd_cnt += 1
            else:
                cnt += odd_cnt
                even_cnt += 1
        return cnt % (10**9 + 7)

s = Solution()
print(s.numOfSubarrays([1,3,5]))
print(s.numOfSubarrays([2,4,6]))
print(s.numOfSubarrays([1,2,3,4,5,6,7]))
print(s.numOfSubarrays([100,100,99,99]))
print(s.numOfSubarrays([7]))
