"""
cumulative sum
choose minimum 2 subarrays

non-overlapping subarrays
(start1, end1), (start2, end2)
end1 <= start2

(TLE)
M: num of subarray O(M^2)
for each subarray:
    find pairs end <= start
    choose sum of length is minimum
"""

from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cum_sum = {0:-1}
        N = len(arr)
        cur = 0
        sub = []
        for i in range(N):
            cur += arr[i]
            remain = cur - target
            if remain in cum_sum:
                sub.append((cum_sum[remain]+1, i))
            cum_sum[cur] = i
        
        sub.sort(key=lambda x: (x[0],x[1]))
        
        min_len = float('inf')
        for i in range(len(sub)):
            start, end = sub[i]
            for _start, _end in sub[i+1:]:
                if end <= _start:
                    min_len = min(min_len, (end-start) + (_end-_start))
        return -1 if min_len == float('inf') else min_len

"""
minimum length subarray from start and from end
<-- min subarray --> i<-- min subarray -->
adding these two length is the answer

time O(N) space O(N)
"""
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        START, END = 0, 1
        def get_mininum_ends(subs):
            min_ends = [0] * N
            cur = 0
            for i in range(N):
                min_len = float('inf')
                while cur < len(subs) and subs[cur][END] <= i:
                    min_len = min(min_len, subs[cur][END] - subs[cur][START] + 1)
                    cur += 1
                if i > 0 and min_len > min_ends[i-1]:
                    min_len = min_ends[i-1]
                min_ends[i] = min_len
            return min_ends
        
        def get_mininum_starts(subs):
            min_starts = [0] * N
            cur = len(subs)-1
            for i in reversed(range(N)):
                min_len = float('inf')
                while cur >= 0 and i < subs[cur][START]:
                    min_len = min(min_len, subs[cur][END] - subs[cur][START] + 1)
                    cur -= 1
                if i < N-1 and min_len > min_starts[i+1]:
                    min_len = min_starts[i+1]
                min_starts[i] = min_len
            return min_starts
        
        cum_sum = {0:-1}
        N = len(arr)
        cur = 0
        subs = []
        for i in range(N):
            cur += arr[i]
            remain = cur - target
            if remain in cum_sum:
                subs.append((cum_sum[remain]+1, i))
            cum_sum[cur] = i
        
        min_ends = get_mininum_ends(subs)
        min_starts = get_mininum_starts(subs)
        # print(min_ends, min_starts)
        
        min_len = float('inf')
        for x, y in zip(min_ends, min_starts):
            min_len = min(x + y, min_len)
        
        return -1 if min_len == float('inf') else min_len

"""
better one pass solution with the same approach above
"""
from itertools import accumulate
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        cum_sum = {0:-1} # {cumulative sum: end index}
        N=len(arr)
        best_till = [float('inf')] * N
        min_len = float('inf')
        for i, _sum in enumerate(accumulate(arr)):
            remain = _sum - target
            if remain in cum_sum:
                start = cum_sum[remain]
                sub_len = i - start
                if start >= 0:
                    min_len = min(min_len, sub_len + best_till[start])
                best_till[i] = sub_len
            if i-1 >= 0:
                best_till[i] = min(best_till[i-1], best_till[i])
                
            cum_sum[_sum] = i
        return -1 if min_len == float('inf') else min_len

s = Solution()
print(s.minSumOfLengths([1,1,1,2,2,2,4,4],6))
print(s.minSumOfLengths([3,2,2,4,3],3))
print(s.minSumOfLengths([7,3,4,7],7))
print(s.minSumOfLengths([4,3,2,6,2,3,4],6))
print(s.minSumOfLengths([5,5,4,4,5],3))
print(s.minSumOfLengths([3,1,1,1,5,1,2,1],3))
