"""
arr = [3,3,3,3,5,5,5,2,2,7]
counter{3:4,5:3,2:2,7:1} -> find the sum of counts which is at least 2/n

time O(NlogN) space O(D),O(N) in worst D: distinct num
"""
from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        removed = 0
        n = len(arr)//2
        
        ans = 0
        for _, c in cnt.most_common():
            removed += c
            ans += 1
            if removed >= n:
                return ans
        return ans

"""
bucket sort
counter values list(bucket)

O(N)
"""
import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        max_val = max(cnt.values())
        n = len(arr)//2
        
        buckets = [0] * (max_val+1)
        
        for c in cnt.values():
            buckets[c] += 1
        
        ans = 0
        for i in reversed(range(max_val+1)):
            removed = i * buckets[i]
            if n - removed <= 0:
                cnt = math.ceil((n) / i)
                ans += cnt
                return ans
            
            n -= removed
            ans += buckets[i]

s = Solution()
print(s.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(s.minSetSize([7,7,7,7,7,7]))
print(s.minSetSize([1,9]))
print(s.minSetSize([1000,1000,3,7]))
print(s.minSetSize([1,2,3,4,5,6,7,8,9,10]))
