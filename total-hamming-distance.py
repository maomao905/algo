"""
4 14 2
0100
1110
0010

look at only the left-most bit
[0,1,0] -> 2

[0,1,0,0] -> 3
[0,1,0,0,0] -> 4
[0,1,0,0,1] -> 6

[0,1,0,1] -> 4
[0,1,0,1,0] -> 6
[0,1,0,1,1] -> 6

if we know the number of occurence of 1, we get the hamming distance
    kC1 * n-kC1 = k * n-k (k is number of 1, n is length of array)

time: O(N*32) = O(N)
space: O(32) = O(1)
"""

from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cnt = [0] * 32
        
        for n in nums:
            i = 0
            while n > 0:
                cnt[i] += (n & 1)
                n >>= 1
                i += 1
        N = len(nums)
        return sum(cnt[i] * (N - cnt[i]) for i in range(len(cnt)))

s = Solution()
print(s.totalHammingDistance([4,14,2]))
