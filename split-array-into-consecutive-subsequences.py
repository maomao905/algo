"""
make sure we have 3 consecutive numbers when initializing subsequence
[1,2,3,3,4,4,5,5]
frequency map
{1:1, 2:1, 3:2, 4:2, 5:2}
next candidate counter map -> if it's set, it will be a problem when there are multiple cands of same number
{}

1 1 is in freq map and 1 is not in cand map, so we create new subarray, which must have 1,2,3
  decrease the freq of 1,2,3 and add 4 as next candidate
  freq: {1:0, 2:0, 3:1, 4:2, 5:2}, cand: {4:1}
2 2's freq is 0, which means we already processed all the 2, skip it
3 3 is in freq map and not in cand, we create new subarray, which must have 3,4,5
  freq: {1:0, 2:0, 3:0, 4:1, 5:1}, cand: {4:1,6:1}
3 3's freq is 0, skip it
4 4 is in cand, update cand
  freq: {1:0, 2:0, 3:0, 4:0, 5:1}, cand: {5:1,6:1}
4 4's freq is now 0, skip it
5 5 is in cand, update cand
  freq: {1:0, 2:0, 3:0, 4:0, 5:0}, cand: {6:2}
5 5's freq is 0, skip it
-> return True
"""

from typing import List
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        cands = Counter()
        
        for n in nums:
            # we've already processed n, skip it
            if freq[n] == 0:
                continue
            # create subsequence, which must have n, n+1, n+2
            if n not in cands or cands[n] == 0:
                for i in range(n, n+3):
                    # number does not exist in the array
                    if freq[i] == 0:
                        return False
                    freq[i] -= 1
                cands[n+3] += 1
            else:
                freq[n] -= 1
                cands[n] -= 1
                cands[n+1] += 1
            # print(n, freq, cands)
        return True

s = Solution()
print(s.isPossible([1,2,3,3,4,4,5]))
print(s.isPossible([1,2,3,3,4,4,5,5]))
print(s.isPossible([1,2,3,4,4,5]))
print(s.isPossible([1,2,3,3,4,5]))
