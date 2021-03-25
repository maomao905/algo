"""
1. store the next element in hashmap
    if next element appear, update the next element (+1)
2. store the min and max to know the length of array
    if the length > k, we need to create another group
3. finally length of groups should be N/k

O(NlogN)
"""

from typing import List
from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        next = defaultdict(list) # {previous or next number and group indexes}
        groups = [] # list of (min, max)
        nums.sort()
        N=len(nums)
        if N % k:
            return False
        elif k == 1:
            return True
        
        for n in nums:
            if next[n]:
                i = next[n].pop()
                if groups[i][1] == n-1:
                    groups[i][1] += 1
                    if groups[i][1] - groups[i][0] + 1 < k:
                        next[n+1].append(i)
            else:
                groups.append([n, n])
                next[n+1].append(len(groups)-1)
        
        return len(groups) == N//k

s = Solution()
print(s.isPossibleDivide([1,2,3,3,4,4,5,6], 4))
print(s.isPossibleDivide([1,2,5,6,3,3,4,4], 4))
print(s.isPossibleDivide([6,2,5,3,4,4,3,1], 4))
print(s.isPossibleDivide([6,2,5,3,3,4,4,3,1], 4))
print(s.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
print(s.isPossibleDivide(nums = [3,3,2,2,1,1], k = 3))
print(s.isPossibleDivide(nums = [1,2,3,4], k = 3))
