"""
1. brute-force (time limit exceeded)
try all combinations
time: O(N^3) two nestd loops * each time sum up to N
"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    cnt += 1
        return cnt

"""
2. sliding window (time limit exceeded)
use previous result
time: O(N^2)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                if current == k:
                    cnt += 1
        return cnt

"""
3. use cumulative sum (time limit exceeded)
calculate the sum of all combinations including first element
then, decrease the start index until the end
time: O(N^2)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        base = 0
        for i in range(len(nums)):
            base += nums[i]
            if base == k:
                cnt += 1
            
            current = base
            for j in range(i):
                current -= nums[j]
                if current == k:
                    cnt += 1
        return cnt

"""
4. cumulative sum hash map
cum_sum[j] - cum_sum[i] = k => sum between i and j is k
e.g.) nums = [3,-3,1,2,3], k=3
  cum_sums = [3, 0,1,3,6]
  例えば、最後のcum_sum=6の場合、cum_sum-k=3となり、3はcum_sumsのindex0とindex3の２つある
  実際に見てみると、-3+1+2+3=3 と 3の２つあるので、正しい
time: O(N)
space: O(N)
"""
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter({0:1})
        s = 0
        for n in nums:
            s += n
            ans += cnt[s-k]
            cnt[s] += 1
        return ans

s = Solution()
print(s.subarraySum([1,1,1],2))
print(s.subarraySum([1,2,3],3))
print(s.subarraySum([3,-3,1,2,3],3))
